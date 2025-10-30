import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

# === FUNCIÓN PARA CALCULAR GC% ===
def GC_content(sequence):
    """Calcula el porcentaje de G y C en una secuencia."""
    gc = sequence.count('G') + sequence.count('C')
    return 100 * gc / len(sequence)

# === FUNCIÓN PARA CALCULAR VALOR P EMPÍRICO ===
def p_value_randomization(sequence, n_sim=1000, fragment_length=1000):
    """
    Calcula un valor p empírico basado en la simulación aleatoria del contenido GC.
    Retorna:
      - GC observado
      - lista de GC simulados
      - valor p empírico
    """
    observed_gc = GC_content(sequence[:fragment_length])
    simulated_gc = []

    for _ in range(n_sim):
        seq_list = list(sequence)
        random.shuffle(seq_list)
        shuffled_seq = "".join(seq_list)[:fragment_length]
        simulated_gc.append(GC_content(shuffled_seq))

    simulated_gc = np.array(simulated_gc)
    p_value = np.mean(simulated_gc >= observed_gc)

    return observed_gc, simulated_gc, p_value


# === CARGAR SECUENCIA ===
filename = "sequencePS.fasta"
sequence = ""
with open(filename) as file:
    next(file)  # saltar encabezado FASTA
    for line in file:
        sequence += line.strip()

# === EJECUCIÓN DEL ANÁLISIS ===
observed_gc, simulated_gc, p_val = p_value_randomization(
    sequence,
    n_sim=1000,
    fragment_length=1000
)

# === IMPRESIÓN DE RESULTADOS ===
print(f"GC% observado: {observed_gc:.2f}%")
print(f"GC% medio aleatorio: {np.mean(simulated_gc):.2f}%")
print(f"Valor p empírico: {p_val:.6f}")

if p_val < 0.05:
    print(" El GC% observado es significativamente diferente del esperado por azar.")
else:
    print(" No hay evidencia de diferencia significativa en el GC% observado.")


# === Visualización, gráfica y estilos===
sns.set_theme(style="darkgrid", context="talk")

plt.figure(figsize=(10, 6))
sns.histplot(simulated_gc, bins=30, kde=True, color="#69b3a2", alpha=0.8)
plt.axvline(observed_gc, color="crimson", linestyle="--", linewidth=3,
            label=f'GC observado: {observed_gc:.2f}%')

plt.title("Distribución del Contenido GC Simulado vs GC Observado",
          fontsize=16, fontweight="bold", family="serif")
plt.xlabel("GC% en secuencias aleatorias", fontsize=13)
plt.ylabel("Frecuencia", fontsize=13)
plt.legend(title=f"Valor p ≈ {p_val:.4g}", fontsize=12, loc="upper left")
plt.tight_layout()
plt.show()
