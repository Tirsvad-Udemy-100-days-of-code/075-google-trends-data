[English](Step-2-Missing-Values) · **Dansk** · [Bahasa Malaysia](Step-2-Missing-Values-ms)

# Trin 2: Manglende værdier

Kun Bitcoin-kursdata har et problem: to værdier er `NaN`, begge i rækken for 2020-08-04 (række 2148). `isna()` finder dem, `.values.any()` fortæller, om der overhovedet er nogen, og summen tæller dem. `dropna()` fjerner rækken.

```python
from google_trends_data.presentation import count_missing, drop_missing

print(count_missing(gateway, DatasetName.BTC_PRICE))  # 2 missing values
drop_missing(gateway, DatasetName.BTC_PRICE)           # 2203 rows remain
```

![Trin 2: Manglende værdier](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-2-missing-values.png)

**Hvad du får:** Hvordan du tæller og lokaliserer manglende værdier og fjerner dem, før de ødelægger et diagram eller en beregning.
