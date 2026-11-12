from collections.abc import Sequence
from datetime import date
from pathlib import Path

from google_trends_data.application.ports import DatasetGateway
from google_trends_data.domain.datasets import (
    CleaningResult,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    Periodicity,
    ResampleResult,
)
from google_trends_data.presentation.screenshots import save_step_screenshots
from google_trends_data.presentation.step_texts import (
    datetime_resample_lines,
    exploration_lines,
    missing_value_lines,
)


class FakeGateway:
    """In-memory DatasetGateway that records the calls it gets."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, DatasetName]] = []

    def summarize(self, name: DatasetName) -> DatasetSummary:
        self.calls.append(("summarize", name))
        return DatasetSummary(name, 3, 2, ("A", "B"), Periodicity.MONTHLY, {})

    def find_missing(self, name: DatasetName) -> MissingReport:
        self.calls.append(("find_missing", name))
        return MissingReport(name, 2, (7,))

    def drop_missing(self, name: DatasetName) -> CleaningResult:
        self.calls.append(("drop_missing", name))
        return CleaningResult(name, 1, 2)

    def convert_dates(self, name: DatasetName) -> DateConversionResult:
        self.calls.append(("convert_dates", name))
        return DateConversionResult(name, "DATE", True)

    def resample_monthly(self, name: DatasetName) -> ResampleResult:
        self.calls.append(("resample_monthly", name))
        return ResampleResult(name, 2, date(2020, 1, 31), date(2020, 2, 29))


class FakeTextRenderer:
    """Records what it is asked to draw instead of drawing it."""

    def __init__(self) -> None:
        self.drawn: list[tuple[str, list[str], Path]] = []

    def render(self, title: str, lines: Sequence[str], output: Path) -> None:
        self.drawn.append((title, list(lines), output))


def test_exploration_lines_summarise_four_datasets_separated_by_blank_lines() -> None:
    gateway: DatasetGateway = FakeGateway()

    lines = exploration_lines(gateway)

    assert lines.count("") == 3
    assert lines[0] == "tesla: 3 rows x 2 columns"
    assert any(line.startswith("btc_price:") for line in lines)
    assert lines[-1] != ""


def test_missing_value_lines_report_rows_then_drop_btc_price() -> None:
    fake = FakeGateway()

    lines = missing_value_lines(fake)

    assert "btc_price: 2 missing values, rows: 7" in lines
    assert fake.calls[-1] == ("drop_missing", DatasetName.BTC_PRICE)
    assert lines[-1] == "drop_missing btc_price: removed 1 row, 2 rows remain"


def test_datetime_resample_lines_convert_all_datasets_then_resample() -> None:
    fake = FakeGateway()

    lines = datetime_resample_lines(fake)

    assert [call for call in fake.calls if call[0] == "convert_dates"] == [
        ("convert_dates", name) for name in DatasetName
    ]
    assert fake.calls[-1] == ("resample_monthly", DatasetName.BTC_PRICE)
    assert "convert_dates tesla: column DATE, datetime True" in lines
    assert lines[-1] == (
        "resample_monthly btc_price: 2 monthly rows, 2020-01-31 to 2020-02-29"
    )


def test_save_step_screenshots_runs_steps_in_lecture_order(tmp_path: Path) -> None:
    fake = FakeGateway()
    renderer = FakeTextRenderer()

    written = save_step_screenshots(fake, renderer, tmp_path)

    assert [path.name for path in written] == [
        "step-1-exploration.png",
        "step-2-missing-values.png",
        "step-3-datetime-resample.png",
    ]
    assert [path for _, _, path in renderer.drawn] == written
    kinds = [kind for kind, _ in fake.calls]
    assert kinds.index("summarize") < kinds.index("find_missing")
    assert kinds.index("drop_missing") < kinds.index("convert_dates")
    assert kinds.index("convert_dates") < kinds.index("resample_monthly")
