import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Estilo visual
sns.set_theme(style="whitegrid")

# Cargar dataset
df = pd.read_csv("Chikungunya.csv")

# Filtrar columnas LC
lc_cols = [c for c in df.columns if "LC" in c]
df_lc = df[lc_cols].apply(pd.to_numeric, errors='coerce').dropna()

# Verificar que haya al menos dos columnas
if len(df_lc.columns) >= 2:
    # Puedes elegir aquí qué columnas usar:
    # Por ejemplo, suponemos que una representa casos confirmados y otra sospechosos
    x_col = df_lc.columns[0]
    y_col = df_lc.columns[1]

    # Crear gráfico JointGrid
    g = sns.JointGrid(data=df_lc, x=x_col, y=y_col, space=0)

    # Densidad principal
    g.plot_joint(
        sns.kdeplot,
        fill=True,
        clip=((df_lc[x_col].min(), df_lc[x_col].max()),
              (df_lc[y_col].min(), df_lc[y_col].max())),
        thresh=0,
        levels=100,
        cmap="rocket"  # Puedes probar: "mako", "flare", "crest"
    )

    # Histogramas laterales
    g.plot_marginals(sns.histplot, color="#2B0B3F", alpha=1, bins=25)

    # Personalizar títulos de los ejes con texto claro
    g.set_axis_labels("Casos Confirmados (LC)", "Casos Sospechosos (LC)",
                      fontsize=12, fontweight="bold")

    # Título general
    plt.suptitle("Relación entre Casos Confirmados y Sospechosos de Chikungunya (LC)",
                 y=1.05, fontsize=14, fontweight="bold")

    # Ajustes para que no se recorten los ejes ni el título
    plt.subplots_adjust(top=0.93, bottom=0.12, left=0.12, right=0.95)
    plt.tight_layout(rect=[0, 0, 1, 0.97])

    # Mostrar gráfico
    plt.show()

else:
    print("No hay suficientes columnas LC para generar el JointGrid.")
