[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu. Kebergantungan masa jalan: `pandas` dan `matplotlib`.

Cipta dan gunakan `.venv` setempat (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jalankan ujian, cipta tangkapan skrin dan buka notebook:

```bash
python -m pytest
python -m google_trends_data.presentation.screenshots
jupyter lab notebooks/google_trends.ipynb
```

**Apa yang anda peroleh:** persediaan yang boleh diulang (satu persekitaran maya bagi setiap projek), pakej yang anda pasang dalam mod boleh disunting (editable), dan ujian yang membuktikan setiap langkah.
