from collections.abc import Iterator
from datetime import date
from pathlib import Path

import matplotlib.dates as mdates
import numpy as np
import pytest
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from google_trends_data.application.chart_specs import (
    bitcoin_chart,
    tesla_basic,
    tesla_with_locators,
    unemployment_2020_chart,
    unemployment_chart,
)
from google_trends_data.domain.charts import (
    ChartSpec,
    GridStyle,
    LineSeries,
    TimeSeries,
)
from google_trends_data.infrastructure.matplotlib_renderer import (
    MatplotlibChartRenderer,
)
from google_trends_data.infrastructure.pandas_gateway import PandasDatasetGateway
from google_trends_data.presentation.lecture import prepare_data

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


@pytest.fixture
def renderer() -> Iterator[MatplotlibChartRenderer]:
    yield MatplotlibChartRenderer()
    plt.close("all")


@pytest.fixture
def prepared(gateway: PandasDatasetGateway) -> PandasDatasetGateway:
    prepare_data(gateway)
    return gateway


def _axes(fig: Figure) -> tuple[Axes, Axes]:
    left, right = fig.axes
    return left, right


def test_build_figure_draws_two_y_axes_with_labels(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(tesla_basic(prepared))

    left, right = _axes(fig)
    assert len(fig.axes) == 2
    assert left.get_ylabel() == "TSLA Stock Price"
    assert right.get_ylabel() == "Search Trend"


def test_build_figure_applies_title_size_limits_and_label_colours(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(tesla_with_locators(prepared))

    left, right = _axes(fig)
    assert left.get_title() == "Tesla Web Search vs Price"
    assert tuple(fig.get_size_inches()) == (14, 8)
    assert fig.dpi == 120
    assert left.get_ylim() == (0, 600)
    assert left.yaxis.label.get_color() == "#E6232E"
    assert right.yaxis.label.get_color() == "skyblue"
    assert left.lines[0].get_linewidth() == 3


def test_build_figure_uses_year_and_month_locators_for_tesla(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(tesla_with_locators(prepared))

    left, _ = _axes(fig)
    assert isinstance(left.xaxis.get_major_locator(), mdates.YearLocator)
    assert isinstance(left.xaxis.get_minor_locator(), mdates.MonthLocator)
    assert isinstance(left.xaxis.get_major_formatter(), mdates.DateFormatter)


def test_build_figure_without_locators_keeps_automatic_date_ticks(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(tesla_basic(prepared))

    left, _ = _axes(fig)
    assert not isinstance(left.xaxis.get_major_locator(), mdates.YearLocator)


def test_build_figure_draws_bitcoin_price_dashed_and_search_with_circles(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(bitcoin_chart(prepared))

    left, right = _axes(fig)
    assert left.lines[0].get_linestyle() == "--"
    assert right.lines[0].get_marker() == "o"
    assert left.get_ylim() == (0, 15000)
    assert isinstance(left.xaxis.get_major_locator(), mdates.YearLocator)
    assert np.asarray(left.lines[0].get_xdata()).size == 73


def test_build_figure_draws_grey_dashed_grid_for_unemployment(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(unemployment_chart(prepared))

    left, _ = _axes(fig)
    lines = left.xaxis.get_gridlines() + left.yaxis.get_gridlines()
    assert all(line.get_color() == "grey" for line in lines)
    assert all(line.get_linestyle() == "--" for line in lines)
    assert left.get_ylim() == (3, 10.5)


def test_build_figure_without_grid_has_no_visible_grid_lines(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway
) -> None:
    fig = renderer.build_figure(unemployment_2020_chart(prepared))

    left, _ = _axes(fig)
    assert not any(line.get_visible() for line in left.yaxis.get_gridlines())


def test_build_figure_accepts_nan_and_missing_title(
    renderer: MatplotlibChartRenderer,
) -> None:
    series = TimeSeries((date(2020, 1, 1), date(2020, 2, 1)), (float("nan"), 1.0))
    spec = ChartSpec(
        title=None,
        left=LineSeries("L", None, series),
        right=LineSeries("R", "red", series),
        grid=GridStyle("grey", ":"),
    )

    fig = renderer.build_figure(spec)

    assert fig.axes[0].get_title() == ""


def test_render_with_output_writes_a_png_file(
    renderer: MatplotlibChartRenderer, prepared: PandasDatasetGateway, tmp_path: Path
) -> None:
    output = tmp_path / "charts" / "tesla.png"

    renderer.render(tesla_basic(prepared), output)

    assert output.read_bytes().startswith(PNG_SIGNATURE)
    assert plt.get_fignums() == []
