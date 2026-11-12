[English](Step-1-Data-Exploration) · [Dansk](Step-1-Data-Exploration-da) · **Bahasa Malaysia**

# Langkah 1: Penerokaan data

Kenali kelima-lima fail CSV sebelum anda mengubah apa-apa.

- **Tesla** mempunyai 124 baris dan 3 lajur: `MONTH`, `TSLA_WEB_SEARCH`, `TSLA_USD_CLOSE`. Lajur carian bernilai antara 2 hingga 31.
- **Pengangguran** mempunyai 181 baris dan 3 lajur: `MONTH`, `UE_BENEFITS_WEB_SEARCH`, `UNRATE`. Nilai carian terbesar ialah 100.
- **Carian Bitcoin** mempunyai 73 baris bulanan; **harga Bitcoin** mempunyai 2204 baris harian dengan `DATE`, `CLOSE` dan `VOLUME`.

Google Trends tidak memberikan bilangan carian. Nilai 100 ialah kemuncak bagi tempoh itu dan 50 bermaksud separuh daripada kepopularan tersebut.

```python
from google_trends_data.domain.datasets import DatasetName
from google_trends_data.presentation import describe_data, format_summary, load_data

gateway = load_data()
print(format_summary(describe_data(gateway, DatasetName.TESLA)))
```

![Langkah 1: Penerokaan data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-1-exploration.png)

**Apa yang anda peroleh:** Bentuk data, nama lajur, nilai minimum dan maksimum dengan `describe()`, serta tempoh bagi setiap siri (bulanan atau harian). Anda juga mengetahui maksud nombor carian Google.
