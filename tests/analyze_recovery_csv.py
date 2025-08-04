import pandas as pd

# Cargar resultados desde el CSV
df = pd.read_csv("logs/recovery_results_1.3-A.csv")

# Filtrar solo hasta 0.50 de ruido
df_filtered = df[df["noise_level"] <= 0.5]

# Agrupar por combinación clave
grouped = df_filtered.groupby(["annealing_start", "repetitions", "chunk_size"])

# Calcular métricas medias
summary = grouped.agg({
    "precision": "mean",
    "exact_match": "mean"
}).reset_index()

# Ordenar por precisión descendente
summary = summary.sort_values(by="precision", ascending=False)

# Mostrar los mejores resultados
print("\n📊 Mejores configuraciones (media de precisión hasta ruido 0.5):")
print(summary.head(10))

# Guardar resultados
summary.to_csv("logs/summary_precision_until_0.5.csv", index=False)
