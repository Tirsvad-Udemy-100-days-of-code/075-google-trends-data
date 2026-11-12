"""Smoke test: the package imports and reports a version."""

import google_trends_data


def test_version_is_defined() -> None:
    assert google_trends_data.__version__ == "0.1.0"
