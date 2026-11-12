**English** · [Dansk](Step-1-Data-Exploration-da) · [Bahasa Malaysia](Step-1-Data-Exploration-ms)

# Step 1: Data exploration

Get to know the five CSV files before you change anything.

- **Tesla** has 124 rows and 3 columns: `MONTH`, `TSLA_WEB_SEARCH`, `TSLA_USD_CLOSE`. The search column runs from 2 to 31.
- **Unemployment** has 181 rows and 3 columns: `MONTH`, `UE_BENEFITS_WEB_SEARCH`, `UNRATE`. The largest search value is 100.
- **Bitcoin search** has 73 monthly rows; **Bitcoin price** has 2204 daily rows with `DATE`, `CLOSE` and `VOLUME`.

Google Trends does not give search counts. A value of 100 is the peak of the period and 50 means half as popular.

```python
from google_trends_data.domain.datasets import DatasetName
from google_trends_data.presentation import describe_data, format_summary, load_data

gateway = load_data()
print(format_summary(describe_data(gateway, DatasetName.TESLA)))
```

![Step 1: Data exploration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/step-1-exploration.png)

**What you gain:** Shape, column names, min and max with `describe()`, and the periodicity of each series (monthly or daily). You also learn what the Google search numbers mean.
