"""The text output of the three data lecture steps, as lines of plain text.

Each function runs its lecture step on the gateway, so call them in lecture order.
"""

from google_trends_data.application.ports import DatasetGateway
from google_trends_data.domain.datasets import DatasetName
from google_trends_data.presentation.lecture import (
    convert_dates,
    count_missing,
    describe_data,
    drop_missing,
    format_summary,
    resample_monthly,
)

EXPLORED = (
    DatasetName.TESLA,
    DatasetName.UNEMPLOYMENT,
    DatasetName.BTC_SEARCH,
    DatasetName.BTC_PRICE,
)
CHECKED_FOR_MISSING = EXPLORED


def exploration_lines(gateway: DatasetGateway) -> list[str]:
    """Step Data Exploration: the summary of each explored dataset."""
    lines: list[str] = []
    for name in EXPLORED:
        lines.extend(format_summary(describe_data(gateway, name)).splitlines())
        lines.append("")
    return lines[:-1]


def missing_value_lines(gateway: DatasetGateway) -> list[str]:
    """Steps Check for Missing Values and Remove Missing Values."""
    lines: list[str] = []
    for name in CHECKED_FOR_MISSING:
        report = count_missing(gateway, name)
        rows = ", ".join(str(row) for row in report.rows_with_missing) or "none"
        lines.append(
            f"{name.value}: {report.missing_values} missing values, rows: {rows}"
        )
    cleaning = drop_missing(gateway, DatasetName.BTC_PRICE)
    lines.append("")
    lines.append(
        f"drop_missing {cleaning.name.value}: removed {cleaning.removed_rows} row, "
        f"{cleaning.remaining_rows} rows remain"
    )
    return lines


def datetime_resample_lines(gateway: DatasetGateway) -> list[str]:
    """Steps Convert Strings to DateTime Objects and Daily to Monthly Data."""
    lines: list[str] = []
    for name in DatasetName:
        conversion = convert_dates(gateway, name)
        lines.append(
            f"convert_dates {name.value}: column {conversion.column}, "
            f"datetime {conversion.is_datetime}"
        )
    monthly = resample_monthly(gateway)
    lines.append("")
    lines.append(
        f"resample_monthly {monthly.name.value}: {monthly.rows} monthly rows, "
        f"{monthly.first_month.isoformat()} to {monthly.last_month.isoformat()}"
    )
    return lines
