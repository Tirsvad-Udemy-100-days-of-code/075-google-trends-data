from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from google_trends_data.domain.datasets import DatasetName, Periodicity
from google_trends_data.domain.errors import (
    DateConversionRequiredError,
    PeriodicityError,
)
from google_trends_data.infrastructure.pandas_gateway import (
    CSV_FILES,
    PandasDatasetGateway,
)


def test_summarize_tesla_gives_shape_and_search_range(
    gateway: PandasDatasetGateway,
) -> None:
    summary = gateway.summarize(DatasetName.TESLA)

    assert (summary.rows, summary.columns) == (124, 3)
    assert summary.periodicity is Periodicity.MONTHLY
    assert summary.statistics["TSLA_WEB_SEARCH"].maximum == 31
    assert summary.statistics["TSLA_WEB_SEARCH"].minimum == 2


def test_summarize_unemployment_gives_shape_and_search_maximum(
    gateway: PandasDatasetGateway,
) -> None:
    summary = gateway.summarize(DatasetName.UNEMPLOYMENT)

    assert (summary.rows, summary.columns) == (181, 3)
    assert summary.periodicity is Periodicity.MONTHLY
    assert summary.statistics["UE_BENEFITS_WEB_SEARCH"].maximum == 100


@pytest.mark.parametrize(
    ("name", "rows", "periodicity"),
    [
        (DatasetName.BTC_SEARCH, 73, Periodicity.MONTHLY),
        (DatasetName.BTC_PRICE, 2204, Periodicity.DAILY),
    ],
)
def test_summarize_bitcoin_gives_rows_and_periodicity(
    gateway: PandasDatasetGateway,
    name: DatasetName,
    rows: int,
    periodicity: Periodicity,
) -> None:
    summary = gateway.summarize(name)

    assert summary.rows == rows
    assert summary.periodicity is periodicity


def test_find_missing_reports_two_values_in_one_btc_price_row(
    gateway: PandasDatasetGateway,
) -> None:
    report = gateway.find_missing(DatasetName.BTC_PRICE)

    assert report.missing_values == 2
    assert report.rows_with_missing == (2148,)


@pytest.mark.parametrize("name", [DatasetName.TESLA, DatasetName.BTC_SEARCH])
def test_find_missing_reports_nothing_for_complete_dataset(
    gateway: PandasDatasetGateway, name: DatasetName
) -> None:
    assert not gateway.find_missing(name).has_missing


def test_drop_missing_removes_the_one_incomplete_row(
    gateway: PandasDatasetGateway,
) -> None:
    result = gateway.drop_missing(DatasetName.BTC_PRICE)

    assert (result.removed_rows, result.remaining_rows) == (1, 2203)
    assert not gateway.find_missing(DatasetName.BTC_PRICE).has_missing


@pytest.mark.parametrize("name", list(DatasetName))
def test_convert_dates_gives_datetime_column(
    gateway: PandasDatasetGateway, name: DatasetName
) -> None:
    result = gateway.convert_dates(name)

    assert result.is_datetime
    assert pd.api.types.is_datetime64_any_dtype(gateway.frame(name)[result.column])


def test_resample_monthly_of_btc_price_gives_73_months(
    gateway: PandasDatasetGateway,
) -> None:
    gateway.drop_missing(DatasetName.BTC_PRICE)
    gateway.convert_dates(DatasetName.BTC_PRICE)

    result = gateway.resample_monthly(DatasetName.BTC_PRICE)

    assert result.rows == 73
    assert result.first_month == date(2014, 9, 30)
    assert result.last_month == date(2020, 9, 30)


def test_monthly_frame_holds_the_resampled_series(
    gateway: PandasDatasetGateway,
) -> None:
    gateway.drop_missing(DatasetName.BTC_PRICE)
    gateway.convert_dates(DatasetName.BTC_PRICE)
    gateway.resample_monthly(DatasetName.BTC_PRICE)

    monthly = gateway.monthly_frame(DatasetName.BTC_PRICE)

    assert monthly.shape[0] == 73
    assert list(monthly.columns) == ["CLOSE", "VOLUME"]


def test_monthly_frame_before_resample_raises_key_error(
    gateway: PandasDatasetGateway,
) -> None:
    with pytest.raises(KeyError):
        gateway.monthly_frame(DatasetName.BTC_PRICE)


def test_resample_before_date_conversion_raises(
    gateway: PandasDatasetGateway,
) -> None:
    with pytest.raises(DateConversionRequiredError):
        gateway.resample_monthly(DatasetName.BTC_PRICE)


def test_resample_of_monthly_dataset_raises(gateway: PandasDatasetGateway) -> None:
    gateway.convert_dates(DatasetName.TESLA)

    with pytest.raises(PeriodicityError):
        gateway.resample_monthly(DatasetName.TESLA)


def test_gateway_reads_csv_from_given_directory(tmp_path: Path) -> None:
    csv = tmp_path / CSV_FILES[DatasetName.BTC_SEARCH]
    csv.write_text("MONTH,BTC_NEWS_SEARCH\n2014-09,5\n2014-10,\n", encoding="utf-8")
    gateway = PandasDatasetGateway(tmp_path)

    summary = gateway.summarize(DatasetName.BTC_SEARCH)
    report = gateway.find_missing(DatasetName.BTC_SEARCH)

    assert summary.rows == 2
    assert report.rows_with_missing == (1,)
