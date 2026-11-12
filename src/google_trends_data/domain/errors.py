"""Errors raised by the domain rules."""


class DataError(Exception):
    """Base class for errors about the lecture data."""


class PeriodicityError(DataError):
    """The operation does not fit the dataset periodicity."""


class DateConversionRequiredError(DataError):
    """The date column must be converted to datetime first."""


class UnknownChartStepError(DataError):
    """No chart exists for the requested lecture step."""
