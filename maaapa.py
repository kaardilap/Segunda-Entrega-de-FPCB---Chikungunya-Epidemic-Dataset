import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # Para leyenda personalizada

# === SHAPEFILE ===
world = gpd.read_file("ne_110m_admin_0_countries.shp")
world = world.to_crs(epsg=4326)
america = world[world['CONTINENT'].isin(['North America', 'South America'])]

# === CARGA DE DATOS ===
df = pd.read_csv("Chikungunya.csv")
for region in ["LC","NLC","CAI","NA","AA","SC"]:
    df[f"Casos_{region}"] = df[f"Conf_{region}"] + df[f"Susp_{region}"].replace("-", 0).astype(int)

# === POSICIONES REPRESENTATIVAS ===
region_coords = {
    "LC": (-60, -15),
    "NLC": (-70, 20),
    "CAI": (-90, 10),
    "NA": (-100, 50),
    "AA": (-70, -5),
    "SC": (-55, -25),
}

colors = {
    "LC": "red",
    "NLC": "orange",
    "CAI": "purple",
    "NA": "green",
    "AA": "cyan",
    "SC": "blue"
}

plt.figure(figsize=(14, 10))
ax = america.plot(color="lightgray", edgecolor="white")

# Añadimos los puntos con escala proporcional
for region, (lon, lat) in region_coords.items():
    total_cases = df[f"Casos_{region}"].sum()
    plt.scatter(
        lon, lat,
        s=total_cases / 5000,  # escala más moderada
        color=colors[region],
        alpha=0.6,
        edgecolor="black",
        linewidth=1.2
    )

# Limitar el mapa
plt.xlim(-130, -30)
plt.ylim(-60, 70)

# Personalización
plt.title("Distribución de Casos de Chikungunya en América por Región", fontsize=10, fontweight="bold")
plt.axis("off")

# === Leyenda personalizada solo con colores ===
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label=f"{region}",
           markerfacecolor=color, markersize=10)
    for region, color in colors.items()
]
plt.legend(handles=legend_elements, title="Región", loc="lower left", bbox_to_anchor=(0, -0.1))

plt.tight_layout()
plt.show()
