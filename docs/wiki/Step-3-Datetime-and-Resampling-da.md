[English](Step-3-Datetime-and-Resampling) · **Dansk** · [Bahasa Malaysia](Step-3-Datetime-and-Resampling-ms)

# Trin 3: Datetime og resampling

Datoer kommer som strenge. `pd.to_datetime` gør dem til rigtige datetimes. Bitcoin-kursen er daglig, men søgedata er månedlige, så `resample("ME")` med `.last()` beholder den sidste kurs i hver måned. Resultatet har 73 rækker, det samme som søgedata.

```python
from google_trends_data.presentation import convert_dates, resample_monthly

convert_dates(gateway, DatasetName.BTC_PRICE)
print(resample_monthly(gateway))  # 73 monthly rows
```

Forelæsningen bruger aliasset `M`; nuværende pandas kalder månedsslut for `ME`.

![Trin 3: Datetime og resampling](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-3-datetime-resample.png)

**Hvad du får:** At gøre to tidsserier sammenlignelige ved at konvertere dem til samme periodicitet, og hvorfor datokolonnen først skal være en datetime.
