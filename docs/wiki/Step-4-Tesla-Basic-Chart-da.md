[English](Step-4-Tesla-Basic-Chart) · **Dansk** · [Bahasa Malaysia](Step-4-Tesla-Basic-Chart-ms)

# Trin 4: Tesla, grundlæggende diagram

Tegn Tesla-aktiekursen mod søgepopulariteten på to y-akser. `twinx()` laver en ekstra y-akse, der deler x-aksen.

```python
from google_trends_data.presentation import create_renderer, draw_chart, prepare_data

prepare_data(gateway)
draw_chart(gateway, create_renderer(), "tesla-1-basic")
```

![Trin 4: Tesla, grundlæggende diagram](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/tesla-1-basic.png)

**Hvad du får:** To akser i ét diagram, så to serier med meget forskellig skala (dollars og et indeks fra 0 til 100) kan sammenlignes.
