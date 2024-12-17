import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn.objects as so
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

df = pd.read_csv(r"C:\Users\Utente\Downloads\contribution-to-eu-27-emissions.csv")
df = df.drop(columns=["AgriLABEL:number", "AgriLABEL:text"])

df.set_index('Emissions:text', inplace=True)
inquinanti_selezionati = ['PM10', 'PM2.5', 'NOx', 'NH3', 'CO']
df_filtrato = df.loc[df.index.isin(inquinanti_selezionati)]

blue_colors = [
    "#a8c6e2",
    "#87a7d4",
    "#6f8fb7",
    "#4e7ea1",
    "#2f6b8a",
    "#1d4f69",
    "#133c4f"
]

new_labels = ['Agricoltura', 'Fornitura di energia', 'Manifatturiero', 'Trasporti non stradali',
              'Residenziale e commerciale', 'Trasporti su strada', 'Rifiuti']

ax = df_filtrato.plot(kind='barh', stacked=True, figsize=(10, 6), color=blue_colors)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Settori",labels=new_labels, fontsize=10)
ax.set_ylabel("")


plt.tight_layout()
plt.show()