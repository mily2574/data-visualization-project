from cProfile import label
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn.objects as so
import seaborn as sns
from categorie import new_labels

dots = pd.read_csv(r"C:\Users\Utente\Downloads\Copia di 260603-FIG2-HRA-INFOGRAPHIC-Six-diseases-v5-Data.csv", sep=";")
dots['PM2.5'] = ["Asma", "Malattia polmonare ostruttiva cronica", "Diabete mellito", "Malattia ischemica del cuore", "Cancro ai polmoni", "Ictus", ]
seconda = pd.read_csv(r"C:\Users\Utente\Downloads\Copia di 260603-FIG2-HRA-INFOGRAPHIC-Six-diseases-v5-Data-2.csv", sep=";")
seconda['NO2'] = ["Asma", "Malattia polmonare ostruttiva cronica", "Diabete mellito", "Malattia ischemica del cuore", "Cancro ai polmoni", "Ictus", ]


blue_colors = [
    "#87a7d4",
    "#4e7ea1",
    "#1d4f69",
    "#133c4f"
]

dots.set_index('PM2.5', inplace=True)
seconda.set_index('NO2', inplace=True)
dots.drop(columns=['DALY'], inplace=True)
seconda.drop(columns=['DALY'], inplace=True)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

dots.plot(kind='barh', stacked=True, ax=axes[0], color=blue_colors)
axes[0].set_title('Particolato <2.5')

seconda.plot(kind='barh', stacked=True, ax=axes[1], color=blue_colors)
axes[1].set_title('Ossidi di azoto')
axes[1].set_yticklabels([])

axes[0].set_xlabel("Anni")
axes[1].set_xlabel("Anni")
axes[0].grid(alpha=0.3)
axes[1].grid( alpha=0.3)


axes[0].set_ylabel("")
plt.suptitle('Impatto della malattia nel 2021',fontsize=16,fontweight='bold')
new_labels = ['Anni di vita persi','Anni vissuti con disabilità']
axes[0].legend(labels = new_labels, loc = "lower right")
axes[1].legend(labels = new_labels, loc = "lower right")
axes[0].set_xlim(0, 800000)
axes[1].set_xlim(0, 800000)

plt.tight_layout()
plt.show()