[English](Step-2-Missing-Values) · [Dansk](Step-2-Missing-Values-da) · **Bahasa Malaysia**

# Langkah 2: Nilai yang hilang

Hanya data harga Bitcoin yang bermasalah: dua nilai ialah `NaN`, kedua-duanya dalam baris 2020-08-04 (baris 2148). `isna()` mencarinya, `.values.any()` memberitahu sama ada wujud nilai sedemikian, dan jumlah (sum) mengira bilangannya. `dropna()` membuang baris itu.

```python
from google_trends_data.presentation import count_missing, drop_missing

print(count_missing(gateway, DatasetName.BTC_PRICE))  # 2 missing values
drop_missing(gateway, DatasetName.BTC_PRICE)           # 2203 rows remain
```

![Langkah 2: Nilai yang hilang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-2-missing-values.png)

**Apa yang anda peroleh:** Cara mengira dan mengesan nilai yang hilang, serta membuangnya, sebelum ia merosakkan carta atau pengiraan.
