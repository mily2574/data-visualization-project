import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="ticks")

dots2 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (4).csv")
dots3 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (7).csv")
dots4 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (8).csv")
dots5 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (9).csv")

media2 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (12).csv")
media3 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (6).csv")
media4 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (11).csv")
media5 = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (10).csv")

palette = sns.color_palette("blend:#EDA,#7AB", as_cmap=False)

for x in range(dots2["TIME_PERIOD"].size) :
    for y in range(media2.size) :
        if dots2["TIME_PERIOD"][x] == media2["TIME_PERIOD"][y] :
            i = dots2["OBS_VALUE"][x] - media2["OBS_VALUE"][y]/27
            dots2.loc[x, "OBS_VALUE"]= i
            break

for x in range(dots3["TIME_PERIOD"].size) :
    for y in range(media3.size) :
        if dots3["TIME_PERIOD"][x] == media3["TIME_PERIOD"][y] :
            i = dots3["OBS_VALUE"][x] - media3["OBS_VALUE"][y]/27
            dots3.loc[x, "OBS_VALUE"]= i
            break

for x in range(dots4["TIME_PERIOD"].size) :
    for y in range(media4.size) :
        if dots4["TIME_PERIOD"][x] == media4["TIME_PERIOD"][y] :
            i = dots3["OBS_VALUE"][x] - media4["OBS_VALUE"][y]/27
            dots4.loc[x, "OBS_VALUE"]= i
            break

for x in range(dots5["TIME_PERIOD"].size) :
    for y in range(media5.size) :
        if dots5["TIME_PERIOD"][x] == media5["TIME_PERIOD"][y] :
            i = dots5["OBS_VALUE"][x] - media5["OBS_VALUE"][y]/27
            dots5.loc[x, "OBS_VALUE"]= i
            break

dataframes = [ (dots2, media2), (dots3, media3),(dots4, media4), (dots5, media5) ]

x_labels = ["Anni", "Anni", "Anni", "Anni", "Anni"]
y_labels = ["Tonnellate di ossidi di azoto", "Tonnellate di ammoniaca", "Tonnellate di particolato < 2.5 micrometri", "Tonnellate di particolato < 2.5 micrometri"]

fig, axes = plt.subplots(2, 2, figsize=(12, 12))

axes = axes.flatten()

for i, (dots, media) in enumerate(dataframes):
    ax = axes[i]
    sns.lineplot(
        data=dots,
        x="TIME_PERIOD", y="OBS_VALUE", hue="geo",
        palette=["lightskyblue", "lightblue", "cyan"], linewidth=3, ax=ax
    )

    ax.plot(
        media["TIME_PERIOD"],
        media["OBS_VALUE"] - media["OBS_VALUE"]
        ,color="black", linestyle="--", linewidth=3, alpha=0.5, label="Media europea"
    )
    ax.set_xlabel(x_labels[i])
    ax.set_ylabel(y_labels[i])
    ax.set_ylim(-500000, 2500000)

    ax.legend(loc="upper right")
    ax.grid(alpha=0.3)



plt.tight_layout()
plt.show()