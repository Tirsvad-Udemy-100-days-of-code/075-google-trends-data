[English](Step-3-Datetime-and-Resampling) · [Dansk](Step-3-Datetime-and-Resampling-da) · **Bahasa Malaysia**

# Langkah 3: Datetime dan resampling

Tarikh diterima sebagai rentetan (string). `pd.to_datetime` menukarnya kepada datetime sebenar. Harga Bitcoin ialah data harian tetapi data carian ialah data bulanan, jadi `resample("ME")` dengan `.last()` mengekalkan harga terakhir bagi setiap bulan. Hasilnya mempunyai 73 baris, sama seperti data carian.

```python
from google_trends_data.presentation import convert_dates, resample_monthly

convert_dates(gateway, DatasetName.BTC_PRICE)
print(resample_monthly(gateway))  # 73 monthly rows
```

Kuliah menggunakan alias `M`; pandas terkini menamakan hujung bulan sebagai `ME`.

![Langkah 3: Datetime dan resampling](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-3-datetime-resample.png)

**Apa yang anda peroleh:** Menjadikan dua siri masa setanding dengan menukarnya kepada tempoh yang sama, dan sebab lajur tarikh mesti ditukar kepada datetime terlebih dahulu.
