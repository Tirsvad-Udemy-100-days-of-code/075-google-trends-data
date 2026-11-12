**English** · [Dansk](Step-2-Missing-Values-da) · [Bahasa Malaysia](Step-2-Missing-Values-ms)

# Step 2: Missing values

Only the Bitcoin price data has a problem: two values are `NaN`, both in the row of 2020-08-04 (row 2148). `isna()` finds them, `.values.any()` tells whether any exist, and the sum counts them. `dropna()` removes the row.

```python
from google_trends_data.presentation import count_missing, drop_missing

print(count_missing(gateway, DatasetName.BTC_PRICE))  # 2 missing values
drop_missing(gateway, DatasetName.BTC_PRICE)           # 2203 rows remain
```

![Step 2: Missing values](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-2-missing-values.png)

**What you gain:** How to count and locate missing values, and to remove them, before they break a chart or a calculation.
