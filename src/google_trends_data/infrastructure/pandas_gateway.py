"""Adapter: the lecture datasets with pandas (see ADR-0001 for why pandas is here)."""

from collections.abc import Mapping
from pathlib import Path

import pandas as pd

from google_trends_data.domain.datasets import (
    DATE_COLUMN,
    PERIODICITY,
    CleaningResult,
    ColumnStatistics,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    ResampleResult,
    ensure_resamplable,
)
from google_trends_data.domain.errors import DateConversionRequiredError

CSV_FILES: Mapping[DatasetName, str] = {
    DatasetName.TESLA: "tesla_search_trend_vs_price.csv",
    DatasetName.UNEMPLOYMENT: "ue_benefits_search_vs_ue_rate_2004_19.csv",
    DatasetName.BTC_SEARCH: "bitcoin_search_trend.csv",
    DatasetName.BTC_PRICE: "daily_bitcoin_price.csv",
    DatasetName.UNEMPLOYMENT_2020: "ue_benefits_search_vs_ue_rate_2004_20.csv",
}


def _column_statistics(described_column: "pd.Series[float]") -> ColumnStatistics:
    """Map one column of `DataFrame.describe()` to the domain statistics."""
    values = described_column.to_dict()
    return ColumnStatistics(
        count=values["count"],
        mean=values["mean"],
        std=values["std"],
        minimum=values["min"],
        maximum=values["max"],
    )


class PandasDatasetGateway:
    """Keeps one DataFrame per dataset, read from CSV on first use."""

    def __init__(self, data_dir: Path) -> None:
        self._data_dir = data_dir
        self._frames: dict[DatasetName, pd.DataFrame] = {}
        self._monthly: dict[DatasetName, pd.DataFrame] = {}

    def frame(self, name: DatasetName) -> pd.DataFrame:
        """Return the current DataFrame of a dataset (reads the CSV once)."""
        if name not in self._frames:
            self._frames[name] = pd.read_csv(self._data_dir / CSV_FILES[name])
        return self._frames[name]

    def monthly_frame(self, name: DatasetName) -> pd.DataFrame:
        """Return the monthly DataFrame made by `resample_monthly`."""
        return self._monthly[name]

    def summarize(self, name: DatasetName) -> DatasetSummary:
        """Return shape, columns, periodicity and `describe()` numbers."""
        frame = self.frame(name)
        described = frame.describe().astype("float64")
        statistics = {
            str(column): _column_statistics(described[column])
            for column in described.columns
        }
        return DatasetSummary(
            name=name,
            rows=frame.shape[0],
            columns=frame.shape[1],
            column_names=tuple(str(column) for column in frame.columns),
            periodicity=PERIODICITY[name],
            statistics=statistics,
        )

    def find_missing(self, name: DatasetName) -> MissingReport:
        """Count NaN values with `isna()` and locate the rows that hold them."""
        frame = self.frame(name)
        rows = frame.index[frame.isna().any(axis=1)]
        return MissingReport(
            name=name,
            missing_values=int(frame.isna().sum().sum()),
            rows_with_missing=tuple(int(row) for row in rows),
        )

    def drop_missing(self, name: DatasetName) -> CleaningResult:
        """Remove rows that contain NaN with `dropna()`."""
        frame = self.frame(name)
        cleaned = frame.dropna()
        self._frames[name] = cleaned
        return CleaningResult(
            name=name,
            removed_rows=frame.shape[0] - cleaned.shape[0],
            remaining_rows=cleaned.shape[0],
        )

    def convert_dates(self, name: DatasetName) -> DateConversionResult:
        """Convert the date column with `pd.to_datetime`."""
        frame = self.frame(name).copy()
        column = DATE_COLUMN[name]
        frame[column] = pd.to_datetime(frame[column])
        self._frames[name] = frame
        return DateConversionResult(
            name=name,
            column=column,
            is_datetime=bool(pd.api.types.is_datetime64_any_dtype(frame[column])),
        )

    def resample_monthly(self, name: DatasetName) -> ResampleResult:
        """Take the last value of each month (month-end alias `ME`)."""
        ensure_resamplable(name)
        frame = self.frame(name)
        column = DATE_COLUMN[name]
        if not pd.api.types.is_datetime64_any_dtype(frame[column]):
            raise DateConversionRequiredError(f"convert {column} of {name.value} first")
        monthly = frame.resample("ME", on=column).last()
        self._monthly[name] = monthly
        return ResampleResult(
            name=name,
            rows=monthly.shape[0],
            first_month=monthly.index.min().date(),
            last_month=monthly.index.max().date(),
        )
