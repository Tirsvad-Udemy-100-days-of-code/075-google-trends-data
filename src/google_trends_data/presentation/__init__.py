"""Presentation layer: the functions a notebook or a script calls."""

from google_trends_data.presentation.bootstrap import load_data
from google_trends_data.presentation.lecture import (
    convert_dates,
    count_missing,
    describe_data,
    drop_missing,
    format_summary,
    resample_monthly,
)

__all__ = [
    "convert_dates",
    "count_missing",
    "describe_data",
    "drop_missing",
    "format_summary",
    "load_data",
    "resample_monthly",
]
