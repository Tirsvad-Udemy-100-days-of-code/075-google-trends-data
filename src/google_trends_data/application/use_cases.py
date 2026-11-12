"""The data preparation steps of the lecture as use cases."""

from google_trends_data.application.ports import DatasetGateway
from google_trends_data.domain.datasets import (
    CleaningResult,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    ResampleResult,
    ensure_resamplable,
)


def explore_dataset(gateway: DatasetGateway, name: DatasetName) -> DatasetSummary:
    """Explore a dataset: shape, column names, periodicity and statistics."""
    return gateway.summarize(name)


def find_missing_values(gateway: DatasetGateway, name: DatasetName) -> MissingReport:
    """Find missing values and the rows that hold them."""
    return gateway.find_missing(name)


def remove_missing_values(gateway: DatasetGateway, name: DatasetName) -> CleaningResult:
    """Remove the rows that contain missing values."""
    return gateway.drop_missing(name)


def convert_date_column(
    gateway: DatasetGateway, name: DatasetName
) -> DateConversionResult:
    """Convert the date strings of a dataset to datetime."""
    return gateway.convert_dates(name)


def resample_to_monthly(gateway: DatasetGateway, name: DatasetName) -> ResampleResult:
    """Resample a daily dataset to monthly data; other periodicities are refused."""
    ensure_resamplable(name)
    return gateway.resample_monthly(name)
