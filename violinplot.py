import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === CARGA DE DATOS ===
df = pd.read_csv("Chikungunya.csv")

# === LIMPIEZA DE DATOS ===
df = df.replace("-", 0)
for col in df.columns:
    if col not in ["Date"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

# === SELECCIÓN DE REGIONES Y CASOS CONFIRMADOS ===
regiones = ["LC", "NLC", "CAI", "NA", "AA", "SC"]
data_violin = pd.DataFrame({
    region: df[f"Conf_{region}"] for region in regiones
})

# === TRANSFORMACIÓN A FORMATO LARGO ===
data_violin = data_violin.melt(var_name="Región", value_name="Casos Confirmados")

# === CONFIGURACIÓN ESTÉTICA ===
sns.set(style="whitegrid", font="serif", context="talk")

plt.figure(figsize=(10, 6))
ax = sns.violinplot(
    data=data_violin,
    x="Región",
    y="Casos Confirmados",
    palette="Spectral",
    inner="box",  # Muestra la caja dentro del violín
    linewidth=1.2
)

# === CÁLCULO DE MEDIAS PARA ANOTACIÓN ===
means = data_violin.groupby("Región")["Casos Confirmados"].mean()

# === ANOTAR LAS MEDIAS ENCIMA DE CADA VIOLÍN ===
for i, region in enumerate(means.index):
    plt.text(i, means[region] + means.max() * 0.02,
             f"{means[region]:.0f}",
             ha="center", va="bottom", fontsize=11, fontweight="bold", color="black", family="serif")

# === PERSONALIZACIÓN ===
plt.title("Distribución de Casos Confirmados de Chikungunya por Región", fontsize=16, fontweight="bold", family="serif")
plt.xlabel("Región", fontsize=13, family="serif")
plt.ylabel("Casos Confirmados", fontsize=13, family="serif")

# === LEYENDA DE MEDIAS ===
leyenda_texto = " | ".join([f"{r}: {v:.0f}" for r, v in means.items()])
plt.text(0.5, -0.15, f"Promedio de casos por región → {leyenda_texto}",
         ha="center", va="center", fontsize=11, family="serif", transform=ax.transAxes)

plt.tight_layout()
plt.show()
