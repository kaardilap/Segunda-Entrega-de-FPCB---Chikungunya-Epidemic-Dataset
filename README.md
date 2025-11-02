#  Análisis del Brote de Chikungunya (2014)

**Autor:** Karina Andrea Ardila Pulgarin  
**Curso:** Programación de las Ciencias Biológicas – 2025  
**Fuente de datos:** Figshare – Brote de Chikungunya en América, 2014  

---

## 📖 Descripción General

Este proyecto realiza un análisis exploratorio y estadístico del **brote de Chikungunya registrado en América durante 2014**, utilizando un conjunto de datos abierto disponible en **Figshare**.  
El estudio incluye la **limpieza de datos**, **visualizaciones estadísticas y geográficas**, y la **aplicación de simulaciones aleatorias** para explorar la distribución de los casos y la variabilidad en distintos contextos.

A través de herramientas de Python, se busca comprender **cómo se comportó la epidemia a nivel regional** y qué patrones o relaciones se pueden observar en la distribución de casos confirmados, sospechosos y fallecimientos.

---

## 🎯 Objetivos del Proyecto

- Procesar y limpiar los datos del brote de Chikungunya (2014).  
- Analizar la distribución de casos confirmados por región.  
- Explorar correlaciones entre diferentes regiones afectadas.  
- Calcular medidas estadísticas, incluyendo simulaciones aleatorias y valores p.  
- Representar los resultados mediante gráficos interpretativos y mapas geográficos.

---


---

## 🧩 Descripción de los Principales Scripts

| Archivo | Descripción |
|----------|--------------|
| **boxplot_horizontal.py** | Muestra la distribución de casos confirmados por región en formato horizontal. |
| **boxplot_vertical.py** | Visualiza la dispersión de casos por región en orientación vertical. |
| **jointgrid.py** | Relación entre casos confirmados y sospechosos (análisis de densidad). |
| **lineplot.py** | Muestra la evolución temporal del brote por semanas epidemiológicas. |
| **heatmap.py** | Mapa de calor para comparar la intensidad del brote en distintas regiones. |

---

## 🧬 Análisis Adicional: Contenido GC y Simulaciones Aleatorias

En la parte complementaria del proyecto, se realiza un **análisis del contenido GC de secuencias genómicas bacterianas** como analogía biológica para comprender la **variabilidad aleatoria y el cálculo de valores p**.  
El código implementa una función que:

1. Calcula el contenido GC de una secuencia real.  
2. Genera miles de secuencias aleatorias del mismo tamaño.  
3. Evalúa la diferencia entre el GC observado y los valores simulados.  
4. Calcula el valor p empírico (significancia estadística).  
5. Muestra un gráfico comparativo de distribución GC.

---

## 🗺️ Impacto del Brote de 2014

El brote de **Chikungunya en 2014** marcó un hito en la salud pública de América, afectando principalmente a países del Caribe, Colombia y América Central.  
Aunque actualmente los brotes son más esporádicos, este evento sigue siendo relevante para:

- Comprender **la expansión de enfermedades transmitidas por mosquitos** (como *Aedes aegypti*).  
- Analizar **patrones epidemiológicos históricos**.  
- Desarrollar **modelos predictivos** frente a nuevos eventos infecciosos.  
- Promover **políticas de control vectorial** y vigilancia sanitaria.

---

## 🧠 Tecnologías Utilizadas

- **Lenguaje:** Python 3.13  
- **Bibliotecas:** Pandas, NumPy, Seaborn, Matplotlib, GeoPandas, Random  
- **Entorno:** PyCharm 


---

✨ *“La bioinformática no solo analiza datos, sino que traduce la historia biológica detrás de ellos.”*


