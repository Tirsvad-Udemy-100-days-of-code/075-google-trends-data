**English** · [Dansk](Step-4-Tesla-Basic-Chart-da) · [Bahasa Malaysia](Step-4-Tesla-Basic-Chart-ms)

# Step 4: Tesla basic chart

Plot the Tesla stock price against the search popularity on two y axes. `twinx()` makes a second y axis that shares the x axis.

```python
from google_trends_data.presentation import create_renderer, draw_chart, prepare_data

prepare_data(gateway)
draw_chart(gateway, create_renderer(), "tesla-1-basic")
```

![Step 4: Tesla basic chart](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/tesla-1-basic.png)

**What you gain:** Two axes in one chart, so two series with very different scales (dollars and a 0 to 100 index) can be compared.
