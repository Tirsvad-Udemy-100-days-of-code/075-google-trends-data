"""Composition root: the one place that builds the pandas adapter."""

from pathlib import Path

from google_trends_data.application.ports import DatasetGateway
from google_trends_data.infrastructure.pandas_gateway import PandasDatasetGateway

DEFAULT_DATA_DIR = Path(__file__).resolve().parents[3] / "data"


def load_data(data_dir: Path | None = None) -> DatasetGateway:
    """Create the gateway that reads the five course CSV files from `data_dir`."""
    return PandasDatasetGateway(data_dir or DEFAULT_DATA_DIR)
