"""Writes one PNG per lecture chart step."""

import logging
import sys
from collections.abc import Sequence
from pathlib import Path

from google_trends_data.application.chart_specs import CHART_STEPS
from google_trends_data.application.ports import ChartRenderer, SeriesSource
from google_trends_data.presentation.bootstrap import create_renderer, load_data
from google_trends_data.presentation.lecture import draw_chart, prepare_data

DEFAULT_IMAGE_DIR = Path(__file__).resolve().parents[3] / "docs" / "images"


def save_chart_screenshots(
    gateway: SeriesSource, renderer: ChartRenderer, directory: Path
) -> list[Path]:
    """Save `<step key>.png` for every chart step; return the files written."""
    directory.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for step in CHART_STEPS:
        output = directory / f"{step}.png"
        draw_chart(gateway, renderer, step, output)
        written.append(output)
    return written


def main(argv: Sequence[str] | None = None) -> None:
    """Prepare the course data and write every chart to a directory."""
    args = list(sys.argv[1:] if argv is None else argv)
    directory = Path(args[0]) if args else DEFAULT_IMAGE_DIR
    logging.basicConfig(level=logging.INFO)
    gateway = load_data()
    prepare_data(gateway)
    save_chart_screenshots(gateway, create_renderer(), directory)


if __name__ == "__main__":
    main()
