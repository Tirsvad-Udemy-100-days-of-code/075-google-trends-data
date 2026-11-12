"""The lecture steps for data exploration and cleaning, as plain functions."""

from google_trends_data.application import use_cases
from google_trends_data.application.ports import DatasetGateway
from google_trends_data.domain.datasets import (
    CleaningResult,
    DatasetName,
    DatasetSummary,
    DateConversionResult,
    MissingReport,
    ResampleResult,
)


def describe_data(gateway: DatasetGateway, name: DatasetName) -> DatasetSummary:
    """Step Data Exploration: shape, column names, min, max and periodicity."""
    return use_cases.explore_dataset(gateway, name)


def count_missing(gateway: DatasetGateway, name: DatasetName) -> MissingReport:
    """Step Check for Missing Values: how many and which rows."""
    return use_cases.find_missing_values(gateway, name)


def drop_missing(gateway: DatasetGateway, name: DatasetName) -> CleaningResult:
    """Step Remove Missing Values."""
    return use_cases.remove_missing_values(gateway, name)


def convert_dates(gateway: DatasetGateway, name: DatasetName) -> DateConversionResult:
    """Step Convert Strings to DateTime Objects."""
    return use_cases.convert_date_column(gateway, name)


def resample_monthly(
    gateway: DatasetGateway, name: DatasetName = DatasetName.BTC_PRICE
) -> ResampleResult:
    """Step Converting from Daily to Monthly Data."""
    return use_cases.resample_to_monthly(gateway, name)


def format_summary(summary: DatasetSummary) -> str:
    """Return the summary as text, one line per fact."""
    lines = [
        f"{summary.name.value}: {summary.rows} rows x {summary.columns} columns",
        f"columns: {', '.join(summary.column_names)}",
        f"periodicity: {summary.periodicity.value}",
    ]
    for column, stats in summary.statistics.items():
        lines.append(f"{column}: min {stats.minimum:g}, max {stats.maximum:g}")
    return "\n".join(lines)
