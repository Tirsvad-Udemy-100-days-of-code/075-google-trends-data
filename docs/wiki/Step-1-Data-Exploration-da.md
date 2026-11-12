[English](Step-1-Data-Exploration) · **Dansk** · [Bahasa Malaysia](Step-1-Data-Exploration-ms)

# Trin 1: Udforskning af data

Lær de fem CSV-filer at kende, før du ændrer noget.

- **Tesla** har 124 rækker og 3 kolonner: `MONTH`, `TSLA_WEB_SEARCH`, `TSLA_USD_CLOSE`. Søgekolonnen går fra 2 til 31.
- **Unemployment** (arbejdsløshed) har 181 rækker og 3 kolonner: `MONTH`, `UE_BENEFITS_WEB_SEARCH`, `UNRATE`. Den største søgeværdi er 100.
- **Bitcoin-søgning** har 73 månedlige rækker; **Bitcoin-kurs** har 2204 daglige rækker med `DATE`, `CLOSE` og `VOLUME`.

Google Trends giver ikke antal søgninger. En værdi på 100 er toppen i perioden, og 50 betyder halvt så populær.

```python
from google_trends_data.domain.datasets import DatasetName
from google_trends_data.presentation import describe_data, format_summary, load_data

gateway = load_data()
print(format_summary(describe_data(gateway, DatasetName.TESLA)))
```

![Trin 1: Udforskning af data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-1-exploration.png)

**Hvad du får:** Form (shape), kolonnenavne, min og max med `describe()` og periodiciteten i hver serie (månedlig eller daglig). Du lærer også, hvad Googles søgetal betyder.
