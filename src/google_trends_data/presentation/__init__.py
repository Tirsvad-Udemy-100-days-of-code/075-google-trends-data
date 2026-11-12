"""Presentation layer: the functions a notebook or a script calls."""

from google_trends_data.presentation.bootstrap import create_renderer, load_data
from google_trends_data.presentation.lecture import (
    convert_dates,
    count_missing,
    describe_data,
    draw_chart,
    drop_missing,
    format_summary,
    prepare_data,
    resample_monthly,
)

__all__ = [
    "convert_dates",
    "count_missing",
    "create_renderer",
    "describe_data",
    "draw_chart",
    "drop_missing",
    "format_summary",
    "load_data",
    "prepare_data",
    "resample_monthly",
]
