import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset y liempieza también
df = pd.read_csv("Chikungunya.csv")
df.columns = df.columns.str.strip()
df.rename(columns={'Epidemiological Week':'Semana'}, inplace=True)
df['Semana'] = pd.to_numeric(df['Semana'], errors='coerce')

# Columnas de casos y muertes por subregión - creación de diccionarios :)
subregiones_casos = {
    'Conf_LC': 'Caribe Latino',
    'Conf_NLC': 'No Caribe Latino',
    'Conf_CAI': 'Istmo Centroamericano',
    'Conf_NA': 'Norte América',
    'Conf_AA': 'Zona Andina',
    'Conf_SC': 'Cono Sur'
}

subregiones_muertes = {
    'Deaths_LC': 'Caribe Latino',
    'Deaths_NLC': 'No Caribe Latino',
    'Deaths_CAI': 'Istmo Centroamericano',
    'Deaths_NA': 'Norte América',
    'Deaths_AA': 'Zona Andina',
    'Deaths_SC': 'Cono Sur'
}

# Agrupar por semana para evitar duplicados
casos_por_semana = df.groupby('Semana')[list(subregiones_casos.keys())].sum()
casos_por_semana.rename(columns=subregiones_casos, inplace=True)

muertes_por_semana = df.groupby('Semana')[list(subregiones_muertes.keys())].sum()
muertes_por_semana.rename(columns=subregiones_muertes, inplace=True)

# Configuración general de Seaborn
sns.set(font_scale=1.1)
plt.figure(figsize=(20,14))

# ---------------- Heatmap de CASOS ---------------- #
plt.subplot(2,1,1)
ax1 = sns.heatmap(
    casos_por_semana.T,
    cmap='Reds',
    annot=True,
    fmt="d",
    linewidths=.5,
    cbar_kws={'label': 'Casos Confirmados'},
    vmin=0,
    vmax=casos_por_semana.max().max(),
    annot_kws={"size":8}
)
ax1.set_title("Casos Semanales de Chikungunya por Subregión", fontsize=18, weight='bold', fontname='Georgia')
ax1.set_xlabel("Semana Epidemiológica", fontsize=14, fontname='Times New Roman', weight='bold')
ax1.set_ylabel("Subregión", fontsize=14, fontname='Times New Roman')
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# ---------------- Heatmap de MUERTES ---------------- #
plt.subplot(2,1,2)
ax2 = sns.heatmap(
    muertes_por_semana.T,
    cmap='Purples',
    annot=True,
    fmt="d",
    linewidths=.5,
    cbar_kws={'label': 'Muertes Confirmadas'},
    vmin=0,
    vmax=muertes_por_semana.max().max(),
    annot_kws={"size":8}
)
ax2.set_title("Muertes Semanales de Chikungunya por Subregión", fontsize=18, weight='bold', fontname='Georgia')
ax2.set_xlabel("Semana Epidemiológica", fontsize=14, fontname='Times New Roman')
ax2.set_ylabel("Subregión", fontsize=14, fontname='Times New Roman')
plt.xticks(rotation=45)
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()
