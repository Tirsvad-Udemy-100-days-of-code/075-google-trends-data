"""Ports: what the use cases need from the outside world."""

from typing import Protocol

from google_trends_data.domain.datasets import (
    CleaningResult,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    ResampleResult,
)


class DatasetGateway(Protocol):
    """Reads and prepares the lecture datasets."""

    def summarize(self, name: DatasetName) -> DatasetSummary:
        """Return shape, columns and statistics."""
        ...

    def find_missing(self, name: DatasetName) -> MissingReport:
        """Return the missing values and their rows."""
        ...

    def drop_missing(self, name: DatasetName) -> CleaningResult:
        """Remove rows with missing values."""
        ...

    def convert_dates(self, name: DatasetName) -> DateConversionResult:
        """Turn the date column into datetimes."""
        ...

    def resample_monthly(self, name: DatasetName) -> ResampleResult:
        """Make a monthly series (last value of the month) from a daily one."""
        ...
