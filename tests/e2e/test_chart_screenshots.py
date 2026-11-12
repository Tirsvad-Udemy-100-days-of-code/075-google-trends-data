from pathlib import Path

from google_trends_data.application.chart_specs import CHART_STEPS
from google_trends_data.presentation.bootstrap import (
    create_renderer,
    load_data,
)
from google_trends_data.presentation.lecture import prepare_data
from google_trends_data.presentation.screenshots import (
    main,
    save_chart_screenshots,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def test_save_chart_screenshots_writes_one_png_per_step(
    data_dir: Path, tmp_path: Path
) -> None:
    gateway = load_data(data_dir)
    prepare_data(gateway)

    written = save_chart_screenshots(gateway, create_renderer(), tmp_path / "images")

    assert len(written) == 8
    assert [path.stem for path in written] == list(CHART_STEPS)
    assert all(path.read_bytes().startswith(PNG_SIGNATURE) for path in written)


def test_main_writes_three_step_images_and_eight_charts(tmp_path: Path) -> None:
    main([str(tmp_path)])

    files = sorted(tmp_path.glob("*.png"))
    assert len(files) == 11
    assert {"step-1-exploration", "step-2-missing-values"} <= {
        path.stem for path in files
    }
    assert all(path.read_bytes().startswith(PNG_SIGNATURE) for path in files)
