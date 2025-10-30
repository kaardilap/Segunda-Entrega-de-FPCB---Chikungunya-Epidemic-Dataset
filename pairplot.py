import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("Chikungunya.csv")

# Filtrar columnas relacionadas con LC y NLC
cols_lc_nlc = [c for c in df.columns if "LC" in c or "NLC" in c]

# Convertir valores no numéricos a 0
for col in cols_lc_nlc:
    df[col] = pd.to_numeric(df[col].replace("-", 0), errors='coerce')

# Filtrar filas donde haya al menos un valor positivo
df_filtered = df[cols_lc_nlc].loc[df[cols_lc_nlc].sum(axis=1) > 0]

# Verificar que haya suficientes columnas
if df_filtered.shape[1] >= 2:
    # Pairplot
    sns.pairplot(df_filtered, palette="coolwarm", diag_kind="hist", kind="scatter")
    plt.suptitle("Pairplot de Casos de Chikungunya - Regiones LC y NLC", y=1.02)
    plt.show()
else:
    print("No hay suficientes datos válidos para generar el pairplot de LC y NLC.")
