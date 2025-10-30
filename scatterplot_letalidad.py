import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# === CARGA DE DATOS ===
df = pd.read_csv("Chikungunya.csv")

# === SELECCIÓN DE DATOS PARA LA REGIÓN AA ===
df["Casos_AA"] = df["Conf_AA"] + df["Susp_AA"]
df["Semana"] = df["Epidemiological Week"]
df = df[["Semana", "Casos_AA", "Deaths_AA"]].copy()

# Eliminar posibles duplicados o NaN
df = df.dropna().drop_duplicates()

# === CÁLCULO DE TASA DE LETALIDAD ===
df["Tasa_Letalidad"] = np.where(df["Casos_AA"] > 0, (df["Deaths_AA"] / df["Casos_AA"]) * 100, 0)
print(f"Tasa promedio de letalidad (AA): {df['Tasa_Letalidad'].mean():.2f}%")

# === CONFIGURACIÓN ESTÉTICA ===
sns.set(style="whitegrid", font="serif", context="talk")

plt.figure(figsize=(10, 6))
ax = sns.scatterplot(
    data=df,
    x="Casos_AA",
    y="Deaths_AA",
    hue="Tasa_Letalidad",
    palette="inferno",
    size="Tasa_Letalidad",
    sizes=(50, 400),
    alpha=0.8,
    edgecolor="black",
)

# === LÍNEA DE TENDENCIA SIN SOMBREADO ===
sns.regplot(
    data=df,
    x="Casos_AA",
    y="Deaths_AA",
    scatter=False,
    ci=None,  # 👈 elimina el sombreado azul
    color="cyan",
    line_kws={"linewidth": 2, "alpha": 0.9},
    order=2  # curva polinómica (puedes probar con 1 o 3)
)

# === PERSONALIZACIÓN ===
plt.title("Región Andina – Relación entre Casos y Muertes de Chikungunya", fontsize=16, fontweight="bold", family="Times New Roman")
plt.xlabel("Casos Confirmados + Sospechosos (Región Andina)", fontsize=13, family="serif")
plt.ylabel("Muertes (Región Andina)", fontsize=13, family="serif")
plt.xticks(rotation=45, fontsize=10, family="serif")
# === BARRA DE COLOR ===
norm = plt.Normalize(vmin=df["Tasa_Letalidad"].min(), vmax=df["Tasa_Letalidad"].max())
sm = plt.cm.ScalarMappable(cmap="inferno", norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label("Tasa de Letalidad (%)", fontsize=12, family="serif")

plt.tight_layout()
plt.show()
