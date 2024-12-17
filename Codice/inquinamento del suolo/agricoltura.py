import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn.objects as so
import seaborn as sns

df = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_gge_filtered_en (1).csv")
media = df.loc[df["geo"] == "European Union - 27 countries (from 2020)"]
df = df.loc[df["geo"] != "European Union - 27 countries (from 2020)"]
df = df.loc[df["TIME_PERIOD"] >= 1990]

g = sns.relplot(
    data=df,
    x="TIME_PERIOD", y="OBS_VALUE", hue="geo", kind="line",
    palette=[ "#A0522D", "#F4A460", "#CD853F",], markers="o", linewidth=3,
)
ax = g.ax
ax.plot(
    media["TIME_PERIOD"],
    media["OBS_VALUE"]/27
    ,color="black", linestyle="--", linewidth=3, alpha=0.5, label="media europea"
)
g._legend.set_loc("upper right")
g._legend.set_title("")
ax.grid(alpha=0.3)
ax.set_xlabel("Anni")
ax.set_ylabel("Tonnellate di gas serra")

plt.tight_layout()
plt.show()

