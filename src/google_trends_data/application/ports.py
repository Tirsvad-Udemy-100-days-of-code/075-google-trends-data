"""Ports: what the use cases need from the outside world."""

from collections.abc import Sequence
from pathlib import Path
from typing import Protocol

from google_trends_data.domain.charts import ChartSpec, TimeSeries
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


class SeriesSource(Protocol):
    """Gives one column of a prepared dataset as a plain time series."""

    def series(
        self,
        name: DatasetName,
        column: str,
        *,
        monthly: bool = False,
        rolling_window: int | None = None,
    ) -> TimeSeries:
        """Return the column; `monthly` reads the resampled data, and
        `rolling_window` replaces each value by the mean of that many months."""
        ...


class ChartRenderer(Protocol):
    """Draws a chart description."""

    def render(self, spec: ChartSpec, output: Path | None = None) -> None:
        """Save the chart to `output` when given, otherwise show it."""
        ...


class TextImageRenderer(Protocol):
    """Draws lines of text as an image."""

    def render(self, title: str, lines: Sequence[str], output: Path) -> None:
        """Save the title and the lines, in monospace, as an image at `output`."""
        ...


class LectureData(DatasetGateway, SeriesSource, Protocol):
    """Everything the lecture needs from the data: preparation and series."""
