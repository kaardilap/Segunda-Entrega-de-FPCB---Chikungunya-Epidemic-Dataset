import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CARGA DE DATOS  Y LIMPIEZA
df = pd.read_csv("Chikungunya.csv")
df = df.replace("-", 0)
for col in df.columns:
    if col not in ["Date"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

# === Cálculo de casos confirmados POR REGIÓN ===
regiones = ["LC", "NLC", "CAI", "NA", "AA", "SC"]
data_boxplot = pd.DataFrame({
    region: df[f"Conf_{region}"] for region in regiones
})

# === Transformacióm a formato largo para reorganizar datos de forma que cada observacion este en su propia fila ===
data_boxplot = data_boxplot.melt(var_name="Región", value_name="Casos Confirmados")

# === Configuracion estetica ===
sns.set(style="whitegrid", font="serif", context="talk")

plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    data=data_boxplot,
    x="Región",
    y="Casos Confirmados",
    palette="Spectral",  # 🎨 Paleta viva y equilibrada
    width=0.6,
    fliersize=5,
    linewidth=1.5
)

# === CÁLCULO DE PROMEDIOS ===
means = data_boxplot.groupby("Región")["Casos Confirmados"].mean().round(1)

# === LEYENDA CON PROMEDIOS (debajo del título) ===
leyenda_texto = "Promedio por región →  " + "   |   ".join([f"{region}: {int(mean):,}" for region, mean in means.items()])

# === TÍTULOS Y ETIQUETAS ===
plt.title("Distribución de Casos Confirmados de Chikungunya por Región",
          fontsize=16, fontweight="bold", family="Times New Roman", pad=25)

# Subtítulo debajo del título
plt.text(
    0.5, 1.02, leyenda_texto,
    ha='center', va='center',
    transform=ax.transAxes,
    fontsize=11, color="dimgray", family="serif"
)

plt.xlabel("Región", fontsize=13, family="serif")
plt.ylabel("Casos Confirmados", fontsize=13, family="serif")

plt.xticks(rotation=30, fontsize=12)
plt.yticks(fontsize=11)
sns.despine(left=False, bottom=False)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # espacio extra arriba para el texto
plt.show()



# === CARGA DE DATOS ===
df = pd.read_csv("Chikungunya.csv")

# === LIMPIEZA DE DATOS ===
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

# === PERSONALIZACIÓN ===
plt.title("Distribución Horizontal de Casos Confirmados de Chikungunya por Región",
          fontsize=14, fontweight="bold", family="Times New Roman")

# Agregar una leyenda de medias debajo del título
leyenda_texto = " | ".join([f"{r}: {v:.0f}" for r, v in means.items()])

plt.xlabel("Casos Confirmados", fontsize=13, family="serif")
plt.ylabel("Región", fontsize=13, family="serif")

# Ajustes visuales
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

