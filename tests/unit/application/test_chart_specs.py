from datetime import date

import pytest

from google_trends_data.application.chart_specs import (
    CHART_STEPS,
    bitcoin_chart,
    build_chart,
    prepare_datasets,
    tesla_basic,
    tesla_coloured,
    tesla_styled,
    tesla_with_locators,
    unemployment_2020_chart,
    unemployment_chart,
    unemployment_rolling_chart,
)
from google_trends_data.domain.charts import TimeSeries
from google_trends_data.domain.datasets import (
    CleaningResult,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    ResampleResult,
)
from google_trends_data.domain.errors import UnknownChartStepError

TESLA_DATES = (date(2010, 6, 1), date(2010, 7, 1), date(2010, 8, 1))
MONTH_ENDS = (date(2014, 9, 30), date(2014, 10, 31))


class FakeSeriesSource:
    """SeriesSource that records requests and returns tiny fixed series."""

    def __init__(self) -> None:
        self.requests: list[tuple[DatasetName, str, bool, int | None]] = []

    def series(
        self,
        name: DatasetName,
        column: str,
        *,
        monthly: bool = False,
        rolling_window: int | None = None,
    ) -> TimeSeries:
        self.requests.append((name, column, monthly, rolling_window))
        if monthly:
            return TimeSeries(MONTH_ENDS, (400.0, 500.0))
        if name is DatasetName.BTC_SEARCH:
            return TimeSeries((date(2014, 9, 1), date(2014, 10, 1)), (5.0, 4.0))
        return TimeSeries(TESLA_DATES, (1.0, 2.0, 3.0))


class FakeGateway:
    """DatasetGateway that records the calls it gets."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, DatasetName]] = []

    def summarize(self, name: DatasetName) -> DatasetSummary:
        raise NotImplementedError

    def find_missing(self, name: DatasetName) -> MissingReport:
        raise NotImplementedError

    def drop_missing(self, name: DatasetName) -> CleaningResult:
        self.calls.append(("drop_missing", name))
        return CleaningResult(name, 1, 2)

    def convert_dates(self, name: DatasetName) -> DateConversionResult:
        self.calls.append(("convert_dates", name))
        return DateConversionResult(name, "DATE", True)

    def resample_monthly(self, name: DatasetName) -> ResampleResult:
        self.calls.append(("resample_monthly", name))
        return ResampleResult(name, 2, MONTH_ENDS[0], MONTH_ENDS[1])


@pytest.fixture
def source() -> FakeSeriesSource:
    return FakeSeriesSource()


def test_tesla_basic_has_two_labelled_axes_without_colours(
    source: FakeSeriesSource,
) -> None:
    spec = tesla_basic(source)

    assert spec.left.axis_label == "TSLA Stock Price"
    assert spec.right.axis_label == "Search Trend"
    assert spec.left.color is None
    assert spec.right.color is None
    assert spec.title is None


def test_tesla_coloured_uses_red_price_and_skyblue_search(
    source: FakeSeriesSource,
) -> None:
    spec = tesla_coloured(source)

    assert spec.left.color == "#E6232E"
    assert spec.right.color == "skyblue"


def test_tesla_styled_applies_lecture_styling(source: FakeSeriesSource) -> None:
    spec = tesla_styled(source)

    assert spec.title == "Tesla Web Search vs Price"
    assert spec.figure_size == (14, 8)
    assert spec.dpi == 120
    assert (spec.label_fontsize, spec.tick_fontsize) == (14, 14)
    assert spec.title_fontsize == 18
    assert spec.x_rotation == 45
    assert spec.left.linewidth == spec.right.linewidth == 3
    assert spec.left_limits == (0, 600)
    assert spec.x_limits == (TESLA_DATES[0], TESLA_DATES[-1])
    assert not spec.year_month_ticks


def test_tesla_with_locators_turns_on_year_month_ticks(
    source: FakeSeriesSource,
) -> None:
    assert tesla_with_locators(source).year_month_ticks


def test_bitcoin_chart_has_dashed_price_and_circle_markers(
    source: FakeSeriesSource,
) -> None:
    spec = bitcoin_chart(source)

    assert spec.title == "Bitcoin News Search vs Resampled Price"
    assert spec.left.axis_label == "BTC Price"
    assert spec.left.color == "#F08F2E"
    assert spec.left.linestyle == "--"
    assert spec.left_limits == (0, 15000)
    assert spec.right.color == "skyblue"
    assert spec.right.marker == "o"
    assert spec.x_limits == MONTH_ENDS
    assert spec.year_month_ticks


def test_bitcoin_chart_plots_search_on_monthly_price_dates(
    source: FakeSeriesSource,
) -> None:
    spec = bitcoin_chart(source)

    assert spec.right.series.dates == MONTH_ENDS
    assert spec.right.series.values == (5.0, 4.0)
    assert (DatasetName.BTC_PRICE, "CLOSE", True, None) in source.requests


def test_unemployment_chart_has_purple_dashed_rate_and_grey_dashed_grid(
    source: FakeSeriesSource,
) -> None:
    spec = unemployment_chart(source)

    assert spec.title is not None
    assert spec.title.startswith('Monthly Search of "Unemployment Benefits"')
    assert spec.left.axis_label == "FRED U/E Rate"
    assert (spec.left.color, spec.left.linestyle) == ("purple", "--")
    assert spec.left_limits == (3, 10.5)
    assert spec.grid is not None
    assert (spec.grid.color, spec.grid.linestyle) == ("grey", "--")
    assert spec.year_month_ticks


def test_unemployment_rolling_chart_asks_for_window_of_six(
    source: FakeSeriesSource,
) -> None:
    spec = unemployment_rolling_chart(source)

    assert spec.title == (
        'Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE'
    )
    assert spec.left.linestyle == "-."
    assert spec.left_limits == (3, 10.5)
    assert [request[3] for request in source.requests] == [6, 6]


def test_unemployment_2020_chart_reads_2020_data_with_solid_lines(
    source: FakeSeriesSource,
) -> None:
    spec = unemployment_2020_chart(source)

    assert {request[0] for request in source.requests} == {
        DatasetName.UNEMPLOYMENT_2020
    }
    assert spec.left.linestyle == spec.right.linestyle == "-"
    assert spec.left_limits is None
    assert spec.title is not None
    assert spec.title.endswith("incl 2020")


def test_chart_steps_have_the_stable_keys() -> None:
    assert list(CHART_STEPS) == [
        "tesla-1-basic",
        "tesla-2-colours",
        "tesla-3-styled",
        "tesla-4-locators",
        "bitcoin",
        "unemployment-grid",
        "unemployment-rolling",
        "unemployment-2020",
    ]


def test_build_chart_with_unknown_step_raises(source: FakeSeriesSource) -> None:
    with pytest.raises(UnknownChartStepError):
        build_chart(source, "nope")


def test_prepare_datasets_cleans_converts_and_resamples() -> None:
    fake = FakeGateway()

    prepare_datasets(fake)

    assert fake.calls[0] == ("drop_missing", DatasetName.BTC_PRICE)
    converted = [name for call, name in fake.calls if call == "convert_dates"]
    assert converted == list(DatasetName)
    assert fake.calls[-1] == ("resample_monthly", DatasetName.BTC_PRICE)
