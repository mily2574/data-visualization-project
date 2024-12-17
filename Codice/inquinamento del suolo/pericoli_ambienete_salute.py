import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn.objects as so
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

produzione = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_chmhaz_filtered_en (3).csv")
consumazione = pd.read_csv(r"C:\Users\Utente\Downloads\estat_env_chmhaz_filtered_en (4).csv")

produzione = produzione.loc[produzione["hazard"] != "Hazardous and non-hazardous - total"]
consumazione = consumazione.loc[consumazione["hazard"] != "Hazardous and non-hazardous - total"]
consumazione = consumazione.loc[consumazione["hazard"] != "Hazardous"]


new_labels = {
    'Carcinogenic, mutagenic and reprotoxic (CMR) health hazard' : 'Rischio per la salute cancerogeno, mutageno e tossico per la riproduzione',
    'Chronic environmental hazard' : 'Pericolo ambientale cronico' ,
    'Chronic toxic health hazard' : 'Pericolo tossico cronico per la salute',
    'Harmful health hazard' : 'Pericolo nocivo per la salute',
    'Hazardous to health' : 'Pericoloso per la salute',
    'Hazardous to the environment' : "Pericoloso per l'ambiente",
    'Moderate chronic environmental hazard' : "Pericolo ambientale cronico moderato",
    'Severe chronic environmental hazard' : "Pericolo ambientale cronico grave",
    'Significant acute environmental hazard' : "Pericolo ambientale acuto significativo",
    'Toxic health hazard' : "Pericolo tossico per la salute",
    'Very toxic health hazard' : "Pericolo altamente tossico per la salute",
    'Significant chronic environmental hazard' : "significativo pericolo ambientale cronico"
}
ordine_personalizzato = [
    'Very toxic health hazard',
    'Toxic health hazard',
    'Carcinogenic, mutagenic and reprotoxic (CMR) health hazard',
    'Chronic toxic health hazard',
    'Harmful health hazard',
    'Hazardous to health',
    'Severe chronic environmental hazard',
    'Significant chronic environmental hazard',
    'Chronic environmental hazard',
    'Moderate chronic environmental hazard',
    'Significant acute environmental hazard',
    'Hazardous to the environment'
]
produzione['hazard'] = pd.Categorical(produzione['hazard'], categories=ordine_personalizzato, ordered=True)
consumazione['hazard'] = pd.Categorical(consumazione['hazard'], categories=ordine_personalizzato, ordered=True)

produzione['hazard'] = produzione['hazard'].replace(new_labels)
consumazione['hazard'] = consumazione['hazard'].replace(new_labels)


g, axes = plt.subplots(1, 2, figsize=(18, 4), gridspec_kw={'width_ratios': [1, 1.20]})
cmap_brown1 = LinearSegmentedColormap.from_list(
    "MarroneChiaroScuro", ["#f4e7d1", "#c19a6b", "#8b4513"]
)
cmap_brown2 = LinearSegmentedColormap.from_list(
    "MarroneVerde", ["#f4e7d1", "#8b7765", "#556b2f"]
)

produzione = produzione.pivot(index='hazard', columns='TIME_PERIOD', values='OBS_VALUE')
consumazione = consumazione.pivot(index='hazard', columns='TIME_PERIOD', values='OBS_VALUE')

sns.heatmap(produzione, ax=axes[0], cmap=cmap_brown1,vmin=0, vmax=275, cbar=False,)
sns.heatmap(consumazione, ax=axes[1], cmap=cmap_brown1,vmin=0, vmax=275, cbar=True, )

axes[1].set_yticklabels([])
axes[0].set_xticklabels([])
axes[1].set_xticklabels([])
axes[0].set_xlabel("")
axes[0].set_ylabel("")
axes[1].set_xlabel("")
axes[1].set_ylabel("")
for ax in axes:
    ax.set_xticks([1, 6, 11, 16])
    ax.set_xticklabels(['2005', '2010', '2015', '2020',], rotation=0)
axes[0].set_title("Produzione", fontsize=18, loc='left')
axes[1].set_title("Consumazione", fontsize=18, loc='left')

plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()