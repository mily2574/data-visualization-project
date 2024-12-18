import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv(r"C:\Users\Utente\Downloads\estat_sdg_11_32_en.csv")

df = df.loc[df["geo"] == "EU27_2020"]
df = df.loc[df["unit"] == "I06"]
df['OBS_VALUE'] = df['OBS_VALUE'].apply(lambda x: x - 100)

g = sns.barplot(
    data=df,
    x="TIME_PERIOD", y="OBS_VALUE"  , color="RosyBrown", ci=None
)
plt.grid(True, which='both',  linewidth=0.3)
plt.xlabel("Anni")
plt.ylabel("percentuale aumentata rispetto al 2006")

plt.tight_layout()
plt.show()

