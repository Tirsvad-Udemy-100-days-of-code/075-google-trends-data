**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer. Runtime dependencies: `pandas` and `matplotlib`.

Create and use a local `.venv` (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the tests, create the screenshots and open the notebook:

```bash
python -m pytest
python -m google_trends_data.presentation.screenshots
jupyter lab notebooks/google_trends.ipynb
```

**What you gain:** a repeatable set-up (a virtual environment per project), a package you install in editable mode, and tests that prove each step.
