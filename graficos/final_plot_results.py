import os
import pandas as pd
import matplotlib.pyplot as plt

# ==== CONFIGURACIÓN ====
csv_path = "logs"  # carpeta donde están los CSVs generados
output_path = "graficos"
os.makedirs(output_path, exist_ok=True)

# ==== ENCUENTRA EL CSV MÁS RECIENTE ====
archivos = [f for f in os.listdir(csv_path) if f.startswith("experimentos_hopfield_") and f.endswith(".csv")]
archivos.sort(reverse=True)
csv_file = archivos[0]
print(f"📄 Usando archivo: {csv_file}")

# ==== CARGA DE DATOS ====
df = pd.read_csv(os.path.join(csv_path, csv_file))

# ==== GRÁFICO 1: PRECISIÓN MEDIA VS RUIDO ====
plt.figure(figsize=(8, 5))
for metodo in df["metodo"].unique():
    df_metodo = df[df["metodo"] == metodo]
    media_precision = df_metodo.groupby("ruido")["precision"].mean()
    plt.plot(media_precision.index, media_precision.values, marker="o", label=metodo)

plt.title("Precisión media vs. nivel de ruido")
plt.xlabel("Nivel de ruido")
plt.ylabel("Precisión (%)")
plt.ylim(0, 105)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_path, "precision_vs_ruido_cifrado.png"))
print("✅ Guardado: precision_vs_ruido_cifrado.png")

# ==== GRÁFICO 2: TASA DE ÉXITO EN DESCIFRADO VS RUIDO ====
plt.figure(figsize=(8, 5))
for metodo in df["metodo"].unique():
    df_metodo = df[df["metodo"] == metodo]
    tasa_exito = df_metodo.groupby("ruido")["exito"].mean() * 100
    plt.plot(tasa_exito.index, tasa_exito.values, marker="s", label=metodo)

plt.title("Tasa de éxito en descifrado vs. nivel de ruido")
plt.xlabel("Nivel de ruido")
plt.ylabel("Mensajes descifrados correctamente (%)")
plt.ylim(0, 105)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_path, "exito_vs_ruido.png"))
print("✅ Guardado: exito_vs_ruido.png")
