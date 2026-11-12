"""Chart descriptions as plain data; a renderer in an adapter draws them."""

from dataclasses import dataclass
from datetime import date

TESLA_RED = "#E6232E"
SKY = "skyblue"
BTC_ORANGE = "#F08F2E"
PURPLE = "purple"
GRID_GREY = "grey"

STYLED_FIGURE_SIZE = (14.0, 8.0)
STYLED_DPI = 120
STYLED_FONT_SIZE = 14
STYLED_TITLE_FONT_SIZE = 18
STYLED_X_ROTATION = 45
STYLED_LINEWIDTH = 3.0


@dataclass(frozen=True, slots=True)
class TimeSeries:
    """Dates with one value each; a value may be NaN (for example a rolling mean)."""

    dates: tuple[date, ...]
    values: tuple[float, ...]


@dataclass(frozen=True, slots=True)
class LineSeries:
    """One line on one y axis, with the label of that axis."""

    axis_label: str
    color: str | None
    series: TimeSeries
    linewidth: float = 1.5
    linestyle: str = "-"
    marker: str | None = None


@dataclass(frozen=True, slots=True)
class GridStyle:
    """Colour and line style of the grid."""

    color: str
    linestyle: str


@dataclass(frozen=True, slots=True)
class ChartSpec:
    """A chart with a left and a right y axis that share the x axis."""

    title: str | None
    left: LineSeries
    right: LineSeries
    figure_size: tuple[float, float] = (6.4, 4.8)
    dpi: int = 100
    label_fontsize: int | None = None
    tick_fontsize: int | None = None
    title_fontsize: int | None = None
    x_rotation: int = 0
    left_limits: tuple[float, float] | None = None
    x_limits: tuple[date, date] | None = None
    year_month_ticks: bool = False
    grid: GridStyle | None = None
