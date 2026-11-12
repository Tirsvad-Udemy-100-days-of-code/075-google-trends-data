[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Krav: Python 3.13 eller nyere. Afhængigheder ved kørsel: `pandas` og `matplotlib`.

Opret og brug et lokalt `.venv` (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Kør testene, opret skærmbillederne og åbn notebooken:

```bash
python -m pytest
python -m google_trends_data.presentation.screenshots
jupyter lab notebooks/google_trends.ipynb
```

**Hvad du får:** en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke, du installerer i editable-tilstand, og tests, der beviser hvert trin.
