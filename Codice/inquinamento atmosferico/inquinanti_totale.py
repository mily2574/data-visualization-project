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
        media["OBS_VALUE"]/27
        ,color="black", linestyle="--", linewidth=3, alpha=0.5, label="Media europea"
    )
    ax.set_xlabel(x_labels[i])
    ax.set_ylabel(y_labels[i])
    ax.set_ylim(-500000, 2500000)

    ax.legend(loc="upper right")
    ax.grid(alpha=0.3)



plt.tight_layout()
plt.show()