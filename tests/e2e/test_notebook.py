import shutil
from pathlib import Path

import nbformat
import pytest
from nbclient.exceptions import CellExecutionError
from nbconvert.preprocessors import ExecutePreprocessor

NOTEBOOK = Path(__file__).resolve().parents[2] / "notebooks" / "google_trends.ipynb"
CELL_TIMEOUT_SECONDS = 300


# pyzmq warns about the default Windows event loop and leaves a socket to the
# garbage collector; both come from the Jupyter client, not from this project.
@pytest.mark.filterwarnings("ignore:Proactor event loop:RuntimeWarning")
@pytest.mark.filterwarnings("ignore:Unclosed socket:ResourceWarning")
@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
def test_notebook_runs_top_to_bottom_without_error(tmp_path: Path) -> None:
    copy = tmp_path / NOTEBOOK.name
    shutil.copy(NOTEBOOK, copy)
    notebook = nbformat.read(copy, as_version=4)  # type: ignore[no-untyped-call]
    executor = ExecutePreprocessor(  # type: ignore[no-untyped-call]
        timeout=CELL_TIMEOUT_SECONDS, kernel_name="python3"
    )

    try:
        executor.preprocess(notebook, {"metadata": {"path": str(tmp_path)}})
    except CellExecutionError as error:  # surface the failing cell in the report
        raise AssertionError(f"notebook cell failed: {error}") from error

    outputs = [
        output
        for cell in notebook.cells
        if cell.cell_type == "code"
        for output in cell.outputs
    ]
    assert not [output for output in outputs if output.output_type == "error"]
    assert sum(1 for output in outputs if output.output_type == "display_data") == 8
