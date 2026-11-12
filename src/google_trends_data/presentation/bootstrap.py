"""Composition root: the one place that builds the pandas and matplotlib adapters."""

from pathlib import Path

from google_trends_data.application.ports import (
    ChartRenderer,
    LectureData,
    TextImageRenderer,
)
from google_trends_data.infrastructure.matplotlib_renderer import (
    MatplotlibChartRenderer,
)
from google_trends_data.infrastructure.pandas_gateway import PandasDatasetGateway
from google_trends_data.infrastructure.text_image_renderer import (
    MatplotlibTextImageRenderer,
)

DEFAULT_DATA_DIR = Path(__file__).resolve().parents[3] / "data"


def load_data(data_dir: Path | None = None) -> LectureData:
    """Create the gateway that reads the five course CSV files from `data_dir`."""
    return PandasDatasetGateway(data_dir or DEFAULT_DATA_DIR)


def create_renderer() -> ChartRenderer:
    """Create the renderer that draws charts with matplotlib."""
    return MatplotlibChartRenderer()


def create_text_renderer() -> TextImageRenderer:
    """Create the renderer that draws lines of text as a PNG."""
    return MatplotlibTextImageRenderer()
