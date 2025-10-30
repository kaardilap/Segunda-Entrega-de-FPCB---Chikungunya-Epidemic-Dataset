import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carga y limpieza de datos
df = pd.read_csv("Chikungunya.csv")
df.columns = df.columns.str.strip()
df.rename(columns={'Epidemiological Week': 'Semana'}, inplace=True)

# Creación de columna de casos totales
df['CasosTotales'] = df[['Conf_LC','Conf_NLC','Conf_CAI','Conf_NA','Conf_AA','Conf_SC']].sum(axis=1)

# Se filtran los datos para eliminar semanas con registros atípicos o sin casos reportados,
# garantizando así un análisis más limpio y representativo.
df = df[(df['CasosTotales'] > 0) & (df['Deaths_LC'] >= 0)]
df = df[df['CasosTotales'] < df['CasosTotales'].quantile(0.98)]

# === Estilo ===
sns.set_style("whitegrid")
plt.figure(figsize=(12,8))

# === Scatterplot ===
scatter = plt.scatter(
    x=df['CasosTotales'],
    y=df['Deaths_LC'],
    s=df['CasosTotales'] * 0.6,
    c=df['Deaths_LC'],
    cmap='plasma',
    alpha=0.85,
    edgecolors='black',
    linewidth=0.7,
    zorder=3
)

# === Línea de tendencia ===
z = np.polyfit(df['CasosTotales'], df['Deaths_LC'], 2)
p = np.poly1d(z)
x_line = np.linspace(df['CasosTotales'].min(), df['CasosTotales'].max(), 200)
plt.plot(x_line, p(x_line), color='cyan', linestyle='--', linewidth=2.2, label='Tendencia polinómica')

# === Barra de color ===
cbar = plt.colorbar(scatter, pad=0.02, aspect=30)
cbar.set_label('Muertes en LC', fontsize=13, weight='bold', fontname='Georgia')
cbar.ax.tick_params(labelsize=10)

# === Etiquetas y estilo ===
plt.title("Relación entre Casos Totales y Muertes por Chikungunya (LC)",
          fontsize=18, fontweight='bold', fontname='Georgia')
plt.xlabel("Casos Totales por Semana", fontsize=14, fontname='Arial')
plt.ylabel("Muertes en LC por Semana", fontsize=14, fontname='Arial')

plt.legend(frameon=True, facecolor='white', edgecolor='gray')
sns.despine(trim=True)
plt.tight_layout()
plt.show()
