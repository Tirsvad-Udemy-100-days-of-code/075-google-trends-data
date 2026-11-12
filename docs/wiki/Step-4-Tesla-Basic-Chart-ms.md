[English](Step-4-Tesla-Basic-Chart) · [Dansk](Step-4-Tesla-Basic-Chart-da) · **Bahasa Malaysia**

# Langkah 4: Carta asas Tesla

Plotkan harga saham Tesla berbanding populariti carian pada dua paksi y. `twinx()` mencipta paksi y kedua yang berkongsi paksi x.

```python
from google_trends_data.presentation import create_renderer, draw_chart, prepare_data

prepare_data(gateway)
draw_chart(gateway, create_renderer(), "tesla-1-basic")
```

![Langkah 4: Carta asas Tesla](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/tesla-1-basic.png)

**Apa yang anda peroleh:** Dua paksi dalam satu carta, supaya dua siri yang skalanya sangat berbeza (dolar dan indeks 0 hingga 100) dapat dibandingkan.
