"""The course datasets, their periodicity and the results of working on them."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from enum import StrEnum

from google_trends_data.domain.errors import PeriodicityError


class DatasetName(StrEnum):
    """The five CSV files of the lecture."""

    TESLA = "tesla"
    UNEMPLOYMENT = "unemployment"
    BTC_SEARCH = "btc_search"
    BTC_PRICE = "btc_price"
    UNEMPLOYMENT_2020 = "unemployment_2020"


class Periodicity(StrEnum):
    """How often a time series has an observation."""

    DAILY = "daily"
    MONTHLY = "monthly"


PERIODICITY: Mapping[DatasetName, Periodicity] = {
    DatasetName.TESLA: Periodicity.MONTHLY,
    DatasetName.UNEMPLOYMENT: Periodicity.MONTHLY,
    DatasetName.BTC_SEARCH: Periodicity.MONTHLY,
    DatasetName.BTC_PRICE: Periodicity.DAILY,
    DatasetName.UNEMPLOYMENT_2020: Periodicity.MONTHLY,
}

DATE_COLUMN: Mapping[DatasetName, str] = {
    DatasetName.TESLA: "MONTH",
    DatasetName.UNEMPLOYMENT: "MONTH",
    DatasetName.BTC_SEARCH: "MONTH",
    DatasetName.BTC_PRICE: "DATE",
    DatasetName.UNEMPLOYMENT_2020: "MONTH",
}


def ensure_resamplable(name: DatasetName) -> None:
    """Only daily data is resampled to monthly data; raise otherwise."""
    if PERIODICITY[name] is not Periodicity.DAILY:
        raise PeriodicityError(f"{name.value} is {PERIODICITY[name].value}, not daily")


@dataclass(frozen=True, slots=True)
class ColumnStatistics:
    """The numbers `describe()` gives for one numeric column."""

    count: float
    mean: float
    std: float
    minimum: float
    maximum: float


@dataclass(frozen=True, slots=True)
class DatasetSummary:
    """Shape, column names, periodicity and statistics of a dataset."""

    name: DatasetName
    rows: int
    columns: int
    column_names: tuple[str, ...]
    periodicity: Periodicity
    statistics: Mapping[str, ColumnStatistics]


@dataclass(frozen=True, slots=True)
class MissingReport:
    """How many values are missing and in which rows (zero-based positions)."""

    name: DatasetName
    missing_values: int
    rows_with_missing: tuple[int, ...]

    @property
    def has_missing(self) -> bool:
        """True when at least one value is missing."""
        return self.missing_values > 0


@dataclass(frozen=True, slots=True)
class CleaningResult:
    """What removing the rows with missing values did."""

    name: DatasetName
    removed_rows: int
    remaining_rows: int


@dataclass(frozen=True, slots=True)
class DateConversionResult:
    """Whether the date column is now a datetime."""

    name: DatasetName
    column: str
    is_datetime: bool


@dataclass(frozen=True, slots=True)
class ResampleResult:
    """The monthly series made from a daily one."""

    name: DatasetName
    rows: int
    first_month: date
    last_month: date
