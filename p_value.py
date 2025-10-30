# ===============================================
# Análisis: cambio en muertes antes vs después del pico
# Dataset de Chikungunya
# ===============================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# ---------------------------------------
# 1. Cargar los datos
# ---------------------------------------
df = pd.read_csv("Chikungunya.csv")

print("\nColumnas detectadas:\n", df.columns.tolist())

# ---------------------------------------
# 2. Usar la columna correcta de semana
# ---------------------------------------
semana_col = 'Epidemiological Week'  # ← esta es tu columna de semanas

# ---------------------------------------
# 3. Crear variable 'Periodo' según el pico
# ---------------------------------------
semana_pico = 30  # ajusta según el gráfico del pico real
df['Periodo'] = df[semana_col].apply(lambda x: 'Antes' if x < semana_pico else 'Después')

# ---------------------------------------
# 4. Escoger una región (ejemplo: Latin Caribbean = LC)
# ---------------------------------------
region = 'LC'
muertes_col = f'Deaths_{region}'

# Elimina filas vacías o NaN
df = df.dropna(subset=[muertes_col])

# ---------------------------------------
# 5. Prueba estadística: Mann–Whitney U test
# ---------------------------------------
muertes_antes = df[df['Periodo'] == 'Antes'][muertes_col]
muertes_despues = df[df['Periodo'] == 'Después'][muertes_col]

stat, p_value = mannwhitneyu(muertes_antes, muertes_despues, alternative='two-sided')

print(f"\nResultado Mann–Whitney U para región {region}:")
print(f"U = {stat:.2f}, p = {p_value:.4f}")

# ---------------------------------------
# 6. Visualización (boxplot)
# ---------------------------------------
sns.set(style="whitegrid", font_scale=1.1)
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='Periodo', y=muertes_col, palette='Set2')
plt.title(f"Muertes antes y después del pico ({region})\nMann–Whitney p = {p_value:.3e}", fontsize=13)
plt.xlabel("Periodo epidemiológico")
plt.ylabel(f"Número de muertes ({region})")
plt.tight_layout()
plt.show()

