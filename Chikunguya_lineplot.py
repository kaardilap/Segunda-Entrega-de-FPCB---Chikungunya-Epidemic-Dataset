import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1️⃣ CARGA Y LIMPIEZA BÁSICA
# ----------------------------
# Cambia el nombre del archivo si es diferente
df = pd.read_csv("Chikungunya.csv", encoding="latin1")

# Normalizar nombres de columnas (sin espacios, todo minúsculas)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
print("Columnas disponibles:", df.columns.tolist())

# ----------------------------
# 2️⃣ CREAR COLUMNA TOTAL_CONFIRMADO (si no existe)
# ----------------------------
if "total_confirmed" not in df.columns:
    # Buscamos todas las columnas que empiecen con 'conf'
    conf_cols = [col for col in df.columns if col.startswith("conf")]
    if conf_cols:
        df["total_confirmed"] = df[conf_cols].apply(pd.to_numeric, errors="coerce").sum(axis=1)
    else:
        raise KeyError("No se encontraron columnas que empiecen con 'Conf'. Revisa tu archivo CSV.")
else:
    df["total_confirmed"] = pd.to_numeric(df["total_confirmed"], errors="coerce")

# Asegurarnos de que 'epidemiological_week' existe
if "epidemiological_week" not in df.columns:
    raise KeyError("No se encontró la columna 'Epidemiological Week' o equivalente. Revisa el archivo CSV.")

# ----------------------------
# 3️⃣ AGRUPAR Y LIMPIAR VALORES
# ----------------------------
df_grouped = (
    df.groupby("epidemiological_week", as_index=False)["total_confirmed"]
    .sum()
    .sort_values("epidemiological_week")
)

# Eliminar outliers extremos (3 desviaciones estándar)
mean = df_grouped["total_confirmed"].mean()
std = df_grouped["total_confirmed"].std()
df_grouped.loc[
    (df_grouped["total_confirmed"] > mean + 3 * std) |
    (df_grouped["total_confirmed"] < mean - 3 * std),
    "total_confirmed"
] = np.nan

# Interpolar valores faltantes
df_grouped["total_confirmed"] = df_grouped["total_confirmed"].interpolate()

# Crear columna suavizada (media móvil 3 semanas)
df_grouped["smoothed"] = df_grouped["total_confirmed"].rolling(window=3, center=True).mean()

# ----------------------------
# 4️⃣ GRAFICAR PROFESIONALMENTE
# ----------------------------
plt.figure(figsize=(12, 7))

# Área debajo de la curva
plt.fill_between(
    df_grouped["epidemiological_week"],
    df_grouped["total_confirmed"],
    color="#f4a7b9", alpha=0.35, label="Impacto acumulado del brote"
)

# Línea de casos
plt.plot(
    df_grouped["epidemiological_week"],
    df_grouped["total_confirmed"],
    color="#c2185b", linewidth=2.5, marker="o", label="Casos confirmados semanales"
)

# Línea de tendencia
plt.plot(
    df_grouped["epidemiological_week"],
    df_grouped["smoothed"],
    color="#880e4f", linestyle="--", linewidth=2.2, label="Tendencia suavizada (3 semanas)"
)

# Semana del pico máximo
max_week = df_grouped.loc[df_grouped["total_confirmed"].idxmax(), "epidemiological_week"]
max_cases = df_grouped["total_confirmed"].max()
plt.axvline(max_week, color="#6a1b9a", linestyle=":", linewidth=2)
plt.text(max_week + 0.5, max_cases * 0.95,
         f"Pico del brote\nSemana {int(max_week)}",
         color="#6a1b9a", fontsize=10, fontweight="bold")

# Estética
plt.title("Evolución semanal del brote de Chikungunya en"
          " América Latina y el Caribe (2014)",
          fontsize=14, weight="bold", pad=20)
plt.xlabel("Semana epidemiológica", fontsize=12)
plt.ylabel("Casos confirmados", fontsize=12)
plt.legend(
    title="Indicadores",
    fontsize=10,
    title_fontsize=10,
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    frameon=True,
    facecolor="white",
    framealpha=0.9,
    edgecolor="#c2185b"
)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Ajusta el área de la figura
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('Evolucion.png')
plt.show()
