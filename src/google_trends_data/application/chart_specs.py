"""The chart of each lecture step, described as plain data."""

from collections.abc import Callable, Mapping
from dataclasses import replace
from datetime import date

from google_trends_data.application import use_cases
from google_trends_data.application.ports import DatasetGateway, SeriesSource
from google_trends_data.domain.charts import (
    BTC_ORANGE,
    GRID_GREY,
    PURPLE,
    SKY,
    STYLED_DPI,
    STYLED_FIGURE_SIZE,
    STYLED_FONT_SIZE,
    STYLED_LINEWIDTH,
    STYLED_TITLE_FONT_SIZE,
    STYLED_X_ROTATION,
    TESLA_RED,
    ChartSpec,
    GridStyle,
    LineSeries,
    TimeSeries,
)
from google_trends_data.domain.datasets import DatasetName
from google_trends_data.domain.errors import UnknownChartStepError

ROLLING_WINDOW_MONTHS = 6
RATE_LIMITS = (3.0, 10.5)
PRICE_LIMITS = (0.0, 600.0)
BITCOIN_PRICE_LIMITS = (0.0, 15000.0)

TESLA_PRICE = "TSLA_USD_CLOSE"
TESLA_SEARCH = "TSLA_WEB_SEARCH"
BTC_PRICE_COLUMN = "CLOSE"
BTC_SEARCH = "BTC_NEWS_SEARCH"
UE_SEARCH = "UE_BENEFITS_WEB_SEARCH"
UE_RATE = "UNRATE"

ChartBuilder = Callable[[SeriesSource], ChartSpec]


def prepare_datasets(gateway: DatasetGateway) -> None:
    """Do the lecture cleaning: drop the missing Bitcoin price, convert the dates
    of all five datasets and resample the Bitcoin price to months."""
    use_cases.remove_missing_values(gateway, DatasetName.BTC_PRICE)
    for name in DatasetName:
        use_cases.convert_date_column(gateway, name)
    use_cases.resample_to_monthly(gateway, DatasetName.BTC_PRICE)


def _x_limits(series: TimeSeries) -> tuple[date, date]:
    return (min(series.dates), max(series.dates))


def _styled(spec: ChartSpec, *, title: str | None = None) -> ChartSpec:
    """Apply the lecture's large figure, fonts, rotated ticks and thick lines."""
    return replace(
        spec,
        title=title if title is not None else spec.title,
        left=replace(spec.left, linewidth=STYLED_LINEWIDTH),
        right=replace(spec.right, linewidth=STYLED_LINEWIDTH),
        figure_size=STYLED_FIGURE_SIZE,
        dpi=STYLED_DPI,
        label_fontsize=STYLED_FONT_SIZE,
        tick_fontsize=STYLED_FONT_SIZE,
        title_fontsize=STYLED_TITLE_FONT_SIZE,
        x_rotation=STYLED_X_ROTATION,
    )


def tesla_basic(source: SeriesSource) -> ChartSpec:
    """Tesla price and search trend on two axes, default colours."""
    price = source.series(DatasetName.TESLA, TESLA_PRICE)
    search = source.series(DatasetName.TESLA, TESLA_SEARCH)
    return ChartSpec(
        title=None,
        left=LineSeries("TSLA Stock Price", None, price),
        right=LineSeries("Search Trend", None, search),
    )


def tesla_coloured(source: SeriesSource) -> ChartSpec:
    """Tesla chart with a red price line and a sky blue search line."""
    basic = tesla_basic(source)
    return replace(
        basic,
        left=replace(basic.left, color=TESLA_RED),
        right=replace(basic.right, color=SKY),
    )


def tesla_styled(source: SeriesSource) -> ChartSpec:
    """Tesla chart with title, fonts, rotated ticks, thick lines and limits."""
    coloured = tesla_coloured(source)
    return replace(
        _styled(coloured, title="Tesla Web Search vs Price"),
        left_limits=PRICE_LIMITS,
        x_limits=_x_limits(coloured.left.series),
    )


def tesla_with_locators(source: SeriesSource) -> ChartSpec:
    """Styled Tesla chart with year and month ticks on the time axis."""
    return replace(tesla_styled(source), year_month_ticks=True)


def bitcoin_chart(source: SeriesSource) -> ChartSpec:
    """Bitcoin news search against the monthly resampled price."""
    price = source.series(DatasetName.BTC_PRICE, BTC_PRICE_COLUMN, monthly=True)
    search = source.series(DatasetName.BTC_SEARCH, BTC_SEARCH)
    # The search is monthly at the start of the month; the lecture plots it on
    # the month-end dates of the resampled price so both lines share the x axis.
    search_on_price_dates = TimeSeries(price.dates, search.values)
    spec = ChartSpec(
        title="Bitcoin News Search vs Resampled Price",
        left=LineSeries("BTC Price", BTC_ORANGE, price, linestyle="--"),
        right=LineSeries("Search Trend", SKY, search_on_price_dates, marker="o"),
        left_limits=BITCOIN_PRICE_LIMITS,
        x_limits=_x_limits(price),
        year_month_ticks=True,
    )
    return _styled(spec)


def _unemployment_spec(
    source: SeriesSource,
    name: DatasetName,
    title: str,
    *,
    rolling_window: int | None = None,
    rate_linestyle: str = "--",
    rate_label: str = "FRED U/E Rate",
) -> ChartSpec:
    rate = source.series(name, UE_RATE, rolling_window=rolling_window)
    search = source.series(name, UE_SEARCH, rolling_window=rolling_window)
    return ChartSpec(
        title=title,
        left=LineSeries(rate_label, PURPLE, rate, linestyle=rate_linestyle),
        right=LineSeries("UE Benefits Search", SKY, search),
        x_limits=_x_limits(rate),
        year_month_ticks=True,
    )


def unemployment_chart(source: SeriesSource) -> ChartSpec:
    """Unemployment benefits search against the rate, with a grey dashed grid."""
    spec = _unemployment_spec(
        source,
        DatasetName.UNEMPLOYMENT,
        'Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate',
    )
    return replace(
        _styled(spec),
        left_limits=RATE_LIMITS,
        grid=GridStyle(GRID_GREY, "--"),
    )


def unemployment_rolling_chart(source: SeriesSource) -> ChartSpec:
    """Six month rolling means of the searches and the unemployment rate."""
    spec = _unemployment_spec(
        source,
        DatasetName.UNEMPLOYMENT,
        'Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE',
        rolling_window=ROLLING_WINDOW_MONTHS,
        rate_linestyle="-.",
        rate_label="UNRATE",
    )
    return replace(_styled(spec), left_limits=RATE_LIMITS)


def unemployment_2020_chart(source: SeriesSource) -> ChartSpec:
    """Unemployment chart including the 2020 pandemic spike."""
    spec = _unemployment_spec(
        source,
        DatasetName.UNEMPLOYMENT_2020,
        'Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020',
        rate_linestyle="-",
    )
    return _styled(spec)


CHART_STEPS: Mapping[str, ChartBuilder] = {
    "tesla-1-basic": tesla_basic,
    "tesla-2-colours": tesla_coloured,
    "tesla-3-styled": tesla_styled,
    "tesla-4-locators": tesla_with_locators,
    "bitcoin": bitcoin_chart,
    "unemployment-grid": unemployment_chart,
    "unemployment-rolling": unemployment_rolling_chart,
    "unemployment-2020": unemployment_2020_chart,
}


def build_chart(source: SeriesSource, step: str) -> ChartSpec:
    """Build the chart of a lecture step; raise for an unknown step key."""
    try:
        builder = CHART_STEPS[step]
    except KeyError:
        known = ", ".join(CHART_STEPS)
        raise UnknownChartStepError(f"unknown step {step!r}; known: {known}") from None
    return builder(source)
