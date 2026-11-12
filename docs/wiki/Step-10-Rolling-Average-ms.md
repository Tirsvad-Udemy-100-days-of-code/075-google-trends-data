[English](Step-10-Rolling-Average) · [Dansk](Step-10-Rolling-Average-da) · **Bahasa Malaysia**

# Langkah 10: Purata bergerak

Volum carian bulanan berubah-ubah. Rolling mean 6 bulan (`.rolling(window=6).mean()`) melicinkannya. Carian yang telah dilicinkan naik sebelum kadar pengangguran naik dan turun sebelum kadar itu turun: carian mendahului, dan kadar ketinggalan. Lima nilai pertama ialah `NaN`, jadi garisan bermula beberapa bulan kemudian.

![Langkah 10: Purata bergerak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/unemployment-rolling.png)

**Apa yang anda peroleh:** Melicinkan data yang bergelora dengan purata bergerak, dan membaca siri mana yang bergerak dahulu.
