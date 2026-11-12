import pytest

from google_trends_data.domain.datasets import (
    PERIODICITY,
    DatasetName,
    MissingReport,
    Periodicity,
    ensure_resamplable,
)
from google_trends_data.domain.errors import PeriodicityError


def test_ensure_resamplable_accepts_daily_dataset() -> None:
    ensure_resamplable(DatasetName.BTC_PRICE)


@pytest.mark.parametrize(
    "name", [name for name in DatasetName if name is not DatasetName.BTC_PRICE]
)
def test_ensure_resamplable_refuses_monthly_dataset(name: DatasetName) -> None:
    with pytest.raises(PeriodicityError):
        ensure_resamplable(name)


def test_periodicity_is_defined_for_every_dataset() -> None:
    assert set(PERIODICITY) == set(DatasetName)
    assert PERIODICITY[DatasetName.BTC_PRICE] is Periodicity.DAILY


def test_has_missing_is_true_when_values_are_missing() -> None:
    report = MissingReport(DatasetName.BTC_PRICE, 2, (5,))

    assert report.has_missing


def test_has_missing_is_false_when_nothing_is_missing() -> None:
    report = MissingReport(DatasetName.TESLA, 0, ())

    assert not report.has_missing
