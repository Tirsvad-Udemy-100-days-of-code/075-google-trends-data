from datetime import date
from pathlib import Path

from google_trends_data.domain.datasets import DatasetName
from google_trends_data.presentation.bootstrap import load_data
from google_trends_data.presentation.lecture import (
    convert_dates,
    count_missing,
    describe_data,
    drop_missing,
    format_summary,
    resample_monthly,
)


def test_lecture_flow_prepares_bitcoin_price_end_to_end(data_dir: Path) -> None:
    gateway = load_data(data_dir)

    summary = describe_data(gateway, DatasetName.BTC_PRICE)
    report = count_missing(gateway, DatasetName.BTC_PRICE)
    cleaning = drop_missing(gateway, DatasetName.BTC_PRICE)
    conversion = convert_dates(gateway, DatasetName.BTC_PRICE)
    monthly = resample_monthly(gateway)

    assert summary.rows == 2204
    assert report.missing_values == 2
    assert cleaning.remaining_rows == 2203
    assert conversion.is_datetime
    assert (monthly.rows, monthly.last_month) == (73, date(2020, 9, 30))


def test_format_summary_lists_shape_and_ranges(data_dir: Path) -> None:
    gateway = load_data(data_dir)

    text = format_summary(describe_data(gateway, DatasetName.TESLA))

    assert "tesla: 124 rows x 3 columns" in text
    assert "periodicity: monthly" in text
    assert "TSLA_WEB_SEARCH: min 2, max 31" in text
