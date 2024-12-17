import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn.objects as so
import seaborn as sns
from grafici import x_labels, y_labels

sns.set_theme(style="ticks")

dots = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (1).csv")
media = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_air_emis_filtered_en (2).csv")

cmap = plt.cm.coolwarm
palette = sns.color_palette("blend:#EDA,#7AB", as_cmap=False)

g = sns.relplot(
        data=dots,
        x="TIME_PERIOD", y="OBS_VALUE", hue="geo", kind="line",
        palette=["lightskyblue", "lightblue", "cyan"], linewidth=3,
    )
ax = g.ax

ax.plot(
        media["TIME_PERIOD"],
        media["OBS_VALUE"]/27
        ,color="black", linestyle="--", linewidth=3, alpha=0.5, label="media europea"
)

g._legend.set_bbox_to_anchor((0.75, 1.0))
g._legend.set_loc("upper center")
g._legend.set_title("")
ax.grid(alpha=0.3)


plt.xlabel("Anni")
plt.ylabel("Tonnellate di monossido di carbonio")

plt.tight_layout()
plt.show()