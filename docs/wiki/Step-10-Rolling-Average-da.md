[English](Step-10-Rolling-Average) · **Dansk** · [Bahasa Malaysia](Step-10-Rolling-Average-ms)

# Trin 10: Glidende gennemsnit

Månedlige søgetal springer rundt. Et glidende gennemsnit over 6 måneder (`.rolling(window=6).mean()`) udjævner dem. De udjævnede søgninger stiger, før arbejdsløshedsprocenten stiger, og falder, før den falder: søgninger fører, og procenten halter efter. De første fem værdier er `NaN`, så linjen starter nogle måneder inde i perioden.

![Trin 10: Glidende gennemsnit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/075-google-trends-data/raw/branch/main/docs/images/unemployment-rolling.png)

**Hvad du får:** Udjævning af støjende data med et glidende gennemsnit, og at aflæse hvilken serie der bevæger sig først.
