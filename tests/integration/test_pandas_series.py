import math
from datetime import date

from google_trends_data.domain.datasets import DatasetName
from google_trends_data.infrastructure.pandas_gateway import PandasDatasetGateway


def test_series_gives_dates_and_float_values_of_tesla(
    gateway: PandasDatasetGateway,
) -> None:
    series = gateway.series(DatasetName.TESLA, "TSLA_WEB_SEARCH")

    assert len(series.dates) == len(series.values) == 124
    assert series.dates[0] == date(2010, 6, 1)
    assert series.values[0] == 3.0
    assert isinstance(series.values[0], float)


def test_series_monthly_gives_73_month_end_points(
    gateway: PandasDatasetGateway,
) -> None:
    gateway.drop_missing(DatasetName.BTC_PRICE)
    gateway.convert_dates(DatasetName.BTC_PRICE)
    gateway.resample_monthly(DatasetName.BTC_PRICE)

    series = gateway.series(DatasetName.BTC_PRICE, "CLOSE", monthly=True)

    assert len(series.dates) == len(series.values) == 73
    assert series.dates[0] == date(2014, 9, 30)
    assert series.dates[-1] == date(2020, 9, 30)


def test_series_rolling_window_six_leaves_five_leading_nan(
    gateway: PandasDatasetGateway,
) -> None:
    plain = gateway.series(DatasetName.UNEMPLOYMENT, "UNRATE")

    rolled = gateway.series(DatasetName.UNEMPLOYMENT, "UNRATE", rolling_window=6)

    assert len(rolled.values) == len(plain.values)
    assert sum(math.isnan(value) for value in rolled.values) == 5
    assert rolled.values[5] == sum(plain.values[:6]) / 6
