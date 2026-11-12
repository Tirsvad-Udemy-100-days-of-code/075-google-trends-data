from pathlib import Path

import pytest

from google_trends_data.infrastructure.pandas_gateway import PandasDatasetGateway


@pytest.fixture
def data_dir() -> Path:
    """The folder with the real course CSV files."""
    return Path(__file__).resolve().parents[1] / "data"


@pytest.fixture
def gateway(data_dir: Path) -> PandasDatasetGateway:
    """A fresh pandas gateway on the real course data."""
    return PandasDatasetGateway(data_dir)
