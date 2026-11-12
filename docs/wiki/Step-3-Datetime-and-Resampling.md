**English** · [Dansk](Step-3-Datetime-and-Resampling-da) · [Bahasa Malaysia](Step-3-Datetime-and-Resampling-ms)

# Step 3: Datetime and resampling

Dates arrive as strings. `pd.to_datetime` turns them into real datetimes. The Bitcoin price is daily but the search data is monthly, so `resample("ME")` with `.last()` keeps the last price of each month. The result has 73 rows, the same as the search data.

```python
from google_trends_data.presentation import convert_dates, resample_monthly

convert_dates(gateway, DatasetName.BTC_PRICE)
print(resample_monthly(gateway))  # 73 monthly rows
```

The lecture uses the alias `M`; current pandas calls month end `ME`.

![Step 3: Datetime and resampling](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-3-datetime-resample.png)

**What you gain:** Making two time series comparable by converting them to the same periodicity, and why the date column must be a datetime first.
