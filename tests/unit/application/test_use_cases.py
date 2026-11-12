from datetime import date

import pytest

from google_trends_data.application.ports import DatasetGateway
from google_trends_data.application.use_cases import (
    convert_date_column,
    explore_dataset,
    find_missing_values,
    remove_missing_values,
    resample_to_monthly,
)
from google_trends_data.domain.datasets import (
    CleaningResult,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    Periodicity,
    ResampleResult,
)
from google_trends_data.domain.errors import PeriodicityError


class FakeGateway:
    """In-memory DatasetGateway that records the calls it gets."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, DatasetName]] = []

    def summarize(self, name: DatasetName) -> DatasetSummary:
        self.calls.append(("summarize", name))
        return DatasetSummary(name, 3, 2, ("A", "B"), Periodicity.MONTHLY, {})

    def find_missing(self, name: DatasetName) -> MissingReport:
        self.calls.append(("find_missing", name))
        return MissingReport(name, 1, (0,))

    def drop_missing(self, name: DatasetName) -> CleaningResult:
        self.calls.append(("drop_missing", name))
        return CleaningResult(name, 1, 2)

    def convert_dates(self, name: DatasetName) -> DateConversionResult:
        self.calls.append(("convert_dates", name))
        return DateConversionResult(name, "DATE", True)

    def resample_monthly(self, name: DatasetName) -> ResampleResult:
        self.calls.append(("resample_monthly", name))
        return ResampleResult(name, 2, date(2020, 1, 31), date(2020, 2, 29))


@pytest.fixture
def fake() -> FakeGateway:
    return FakeGateway()


def test_explore_dataset_returns_gateway_summary(fake: FakeGateway) -> None:
    gateway: DatasetGateway = fake

    summary = explore_dataset(gateway, DatasetName.TESLA)

    assert summary.rows == 3
    assert fake.calls == [("summarize", DatasetName.TESLA)]


def test_find_missing_values_returns_gateway_report(fake: FakeGateway) -> None:
    report = find_missing_values(fake, DatasetName.BTC_PRICE)

    assert report.has_missing
    assert fake.calls == [("find_missing", DatasetName.BTC_PRICE)]


def test_remove_missing_values_returns_gateway_result(fake: FakeGateway) -> None:
    result = remove_missing_values(fake, DatasetName.BTC_PRICE)

    assert (result.removed_rows, result.remaining_rows) == (1, 2)


def test_convert_date_column_returns_gateway_result(fake: FakeGateway) -> None:
    result = convert_date_column(fake, DatasetName.BTC_PRICE)

    assert result.is_datetime


def test_resample_to_monthly_delegates_for_daily_dataset(fake: FakeGateway) -> None:
    result = resample_to_monthly(fake, DatasetName.BTC_PRICE)

    assert result.rows == 2
    assert fake.calls == [("resample_monthly", DatasetName.BTC_PRICE)]


def test_resample_to_monthly_refuses_monthly_dataset(fake: FakeGateway) -> None:
    with pytest.raises(PeriodicityError):
        resample_to_monthly(fake, DatasetName.BTC_SEARCH)

    assert fake.calls == []
