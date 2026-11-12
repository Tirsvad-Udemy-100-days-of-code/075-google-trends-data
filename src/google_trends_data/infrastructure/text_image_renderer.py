"""Adapter: draws lines of text as a PNG with matplotlib (Agg, no window)."""

import logging
from collections.abc import Sequence
from pathlib import Path

from matplotlib.figure import Figure

logger = logging.getLogger(__name__)

FIGURE_WIDTH = 14.0
DPI = 120
FONT_SIZE = 12
TITLE_FONT_SIZE = 15
LINE_HEIGHT_INCHES = 0.27
MARGIN_INCHES = 0.4
BACKGROUND = "#f7f7f2"
TEXT_COLOR = "#222222"


class MatplotlibTextImageRenderer:
    """Turns a title and lines of text into a monospace PNG on a light page."""

    def render(self, title: str, lines: Sequence[str], output: Path) -> None:
        """Save the title and the lines as an image at `output`."""
        # Figure is used without pyplot, so no global state or window is created.
        height = (len(lines) + 2) * LINE_HEIGHT_INCHES + 2 * MARGIN_INCHES
        fig = Figure(figsize=(FIGURE_WIDTH, height), dpi=DPI, facecolor=BACKGROUND)
        top = 1 - MARGIN_INCHES / height
        step = LINE_HEIGHT_INCHES / height
        fig.text(
            MARGIN_INCHES / FIGURE_WIDTH,
            top,
            title,
            family="monospace",
            fontsize=TITLE_FONT_SIZE,
            fontweight="bold",
            color=TEXT_COLOR,
            va="top",
        )
        for index, line in enumerate(lines, start=2):
            fig.text(
                MARGIN_INCHES / FIGURE_WIDTH,
                top - index * step,
                line,
                family="monospace",
                fontsize=FONT_SIZE,
                color=TEXT_COLOR,
                va="top",
            )
        output.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output, facecolor=BACKGROUND)
        logger.info("saved text image %s", output)
