"""Adapter: draws chart specs with matplotlib."""

import logging
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from google_trends_data.domain.charts import ChartSpec, LineSeries

logger = logging.getLogger(__name__)


def _draw_line(ax: Axes, line: LineSeries, spec: ChartSpec) -> None:
    ax.plot(
        np.array(line.series.dates, dtype="datetime64[D]"),
        np.array(line.series.values, dtype="float64"),
        color=line.color,
        linewidth=line.linewidth,
        linestyle=line.linestyle,
        marker=line.marker,
    )
    ax.set_ylabel(line.axis_label, fontsize=spec.label_fontsize)
    if line.color is not None:
        ax.yaxis.label.set_color(line.color)
    if spec.tick_fontsize is not None:
        ax.tick_params(axis="y", labelsize=spec.tick_fontsize)


def _style_time_axis(ax: Axes, spec: ChartSpec) -> None:
    ax.tick_params(axis="x", labelrotation=spec.x_rotation)
    if spec.tick_fontsize is not None:
        ax.tick_params(axis="x", labelsize=spec.tick_fontsize)
    if spec.year_month_ticks:
        # matplotlib.dates ships no type hints for these constructors.
        ax.xaxis.set_major_locator(mdates.YearLocator())  # type: ignore[no-untyped-call]
        ax.xaxis.set_minor_locator(mdates.MonthLocator())  # type: ignore[no-untyped-call]
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # type: ignore[no-untyped-call]
    if spec.x_limits is not None:
        first, last = spec.x_limits
        ax.set_xlim(
            float(mdates.date2num(first)),  # type: ignore[no-untyped-call]
            float(mdates.date2num(last)),  # type: ignore[no-untyped-call]
        )


class MatplotlibChartRenderer:
    """Turns a `ChartSpec` into a matplotlib figure, a PNG file or a window."""

    def build_figure(self, spec: ChartSpec) -> Figure:
        """Draw the spec; the left axis is `axes[0]`, the right one `axes[1]`."""
        fig = plt.figure(figsize=spec.figure_size, dpi=spec.dpi)
        left_ax = fig.add_subplot()
        right_ax = left_ax.twinx()
        _draw_line(left_ax, spec.left, spec)
        _draw_line(right_ax, spec.right, spec)
        _style_time_axis(left_ax, spec)
        if spec.left_limits is not None:
            left_ax.set_ylim(spec.left_limits)
        if spec.title is not None:
            left_ax.set_title(spec.title, fontsize=spec.title_fontsize)
        if spec.grid is not None:
            left_ax.grid(color=spec.grid.color, linestyle=spec.grid.linestyle)
        return fig

    def render(self, spec: ChartSpec, output: Path | None = None) -> None:
        """Save the chart to `output` when given, otherwise show it."""
        fig = self.build_figure(spec)
        try:
            if output is None:
                plt.show()
            else:
                output.parent.mkdir(parents=True, exist_ok=True)
                fig.savefig(output, bbox_inches="tight")
                logger.info("saved chart %s", output)
        finally:
            plt.close(fig)
