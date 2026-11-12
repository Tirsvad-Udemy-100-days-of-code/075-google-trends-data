"""Writes one PNG per lecture step: three text steps and eight chart steps."""

import logging
import sys
from collections.abc import Callable, Sequence
from pathlib import Path

from google_trends_data.application.chart_specs import CHART_STEPS
from google_trends_data.application.ports import (
    ChartRenderer,
    DatasetGateway,
    SeriesSource,
    TextImageRenderer,
)
from google_trends_data.presentation.bootstrap import (
    create_renderer,
    create_text_renderer,
    load_data,
)
from google_trends_data.presentation.lecture import draw_chart, prepare_data
from google_trends_data.presentation.step_texts import (
    datetime_resample_lines,
    exploration_lines,
    missing_value_lines,
)

DEFAULT_IMAGE_DIR = Path(__file__).resolve().parents[3] / "docs" / "images"

# (file name without extension, image title, lines of the step), in lecture order.
TEXT_STEPS: tuple[tuple[str, str, Callable[[DatasetGateway], list[str]]], ...] = (
    ("step-1-exploration", "Data Exploration", exploration_lines),
    ("step-2-missing-values", "Missing Values", missing_value_lines),
    (
        "step-3-datetime-resample",
        "Convert to DateTime and Resample",
        datetime_resample_lines,
    ),
)


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


def save_step_screenshots(
    gateway: DatasetGateway, renderer: TextImageRenderer, directory: Path
) -> list[Path]:
    """Run the data steps in lecture order on `gateway` and save the text of each
    as `<step>.png`; return the files written."""
    written: list[Path] = []
    for key, title, build_lines in TEXT_STEPS:
        output = directory / f"{key}.png"
        renderer.render(title, build_lines(gateway), output)
        written.append(output)
    return written


def main(argv: Sequence[str] | None = None) -> None:
    """Prepare the course data and write every step image to a directory."""
    args = list(sys.argv[1:] if argv is None else argv)
    directory = Path(args[0]) if args else DEFAULT_IMAGE_DIR
    logging.basicConfig(level=logging.INFO)
    gateway = load_data()
    save_step_screenshots(gateway, create_text_renderer(), directory)
    prepare_data(gateway)
    save_chart_screenshots(gateway, create_renderer(), directory)


if __name__ == "__main__":
    main()
