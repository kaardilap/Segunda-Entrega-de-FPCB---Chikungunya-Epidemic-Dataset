import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CARGA DE DATOS y LIMPIEZA ===
df = pd.read_csv("Chikungunya.csv")

df = df.replace("-", 0)
for col in df.columns:
    if col not in ["Date"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

# === SELECCIÓN DE REGIONES Y CASOS CONFIRMADOS ===
regiones = ["LC", "NLC", "CAI", "NA", "AA", "SC"]
data_box = pd.DataFrame({
    region: df[f"Conf_{region}"] for region in regiones
})

# === TRANSFORMACIÓN A FORMATO LARGO ===
data_box = data_box.melt(var_name="Región", value_name="Casos Confirmados")

# === CONFIGURACIÓN ESTÉTICA ===
sns.set(style="whitegrid", font="serif", context="talk")

plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    data=data_box,
    y="Región",
    x="Casos Confirmados",
    palette="Spectral",
    width=0.6,
    fliersize=0,  # ocultamos los outliers, ya se verán con los puntos
)

# === AÑADIR OBSERVACIONES INDIVIDUALES ===
sns.stripplot(
    data=data_box,
    y="Región",
    x="Casos Confirmados",
    color="black",
    alpha=0.5,
    size=4,
    jitter=True
)

# === CALCULAR MEDIAS ===
means = data_box.groupby("Región")["Casos Confirmados"].mean()

# === PERSONALIZACIÓN y mas esteticaaaa ===
plt.title("Distribución Horizontal de Casos Confirmados de Chikungunya por Región",
          fontsize=16, fontweight="bold", family="serif")

# Agregar una leyenda de medias debajo del título
leyenda_texto = " | ".join([f"{r}: {v:.0f}" for r, v in means.items()])
plt.text(0.5, 1.03, f"Promedio de casos por región → {leyenda_texto}",
         ha="center", va="bottom", fontsize=11, family="serif", transform=ax.transAxes)

plt.xlabel("Casos Confirmados", fontsize=13, family="serif")
plt.ylabel("Región", fontsize=13, family="serif")

# Ajustes visuales
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
