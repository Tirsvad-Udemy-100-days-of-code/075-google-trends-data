**English** · [Dansk](Step-10-Rolling-Average-da) · [Bahasa Malaysia](Step-10-Rolling-Average-ms)

# Step 10: Rolling average

Monthly search volume jumps around. A 6-month rolling mean (`.rolling(window=6).mean()`) smooths it. The smoothed searches rise before the unemployment rate rises and fall before it falls: searches lead, and the rate lags. The first five values are `NaN`, so the line starts a few months in.

![Step 10: Rolling average](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/unemployment-rolling.png)

**What you gain:** Smoothing noisy data with a rolling average, and reading which series moves first.
