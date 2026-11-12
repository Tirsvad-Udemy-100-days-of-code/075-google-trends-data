from pathlib import Path

from google_trends_data.infrastructure.text_image_renderer import (
    MatplotlibTextImageRenderer,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def test_render_writes_a_png_with_the_configured_width(tmp_path: Path) -> None:
    output = tmp_path / "images" / "step.png"

    MatplotlibTextImageRenderer().render("Title", ["first", "second"], output)

    data = output.read_bytes()
    assert data.startswith(PNG_SIGNATURE)
    width = int.from_bytes(data[16:20], "big")
    assert width == 14 * 120


def test_render_accepts_no_lines(tmp_path: Path) -> None:
    output = tmp_path / "empty.png"

    MatplotlibTextImageRenderer().render("Only a title", [], output)

    assert output.read_bytes().startswith(PNG_SIGNATURE)
