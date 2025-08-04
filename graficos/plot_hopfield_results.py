import os
import pandas as pd
import matplotlib.pyplot as plt

def cargar_y_preparar_datos(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df = df[["version", "noise_level", "precision"]]
    return df

def agrupar_datos(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["version", "noise_level"])["precision"].agg(["mean", "std"]).reset_index()

def graficar(df_agg: pd.DataFrame, output_path: str):
    versiones = df_agg["version"].unique()
    colores = ["blue", "green", "orange", "red"]

    plt.figure(figsize=(10, 6))

    for i, version in enumerate(versiones):
        subset = df_agg[df_agg["version"] == version]
        plt.plot(subset["noise_level"], subset["mean"], label=f"Versión {version}", color=colores[i % len(colores)])
        plt.fill_between(subset["noise_level"], 
                         subset["mean"] - subset["std"], 
                         subset["mean"] + subset["std"], 
                         alpha=0.2, color=colores[i % len(colores)])

    plt.xlabel("Nivel de ruido")
    plt.ylabel("Precisión media (%)")
    plt.title("Precisión vs Nivel de Ruido (Hopfield)")
    plt.grid(True)
    plt.legend()
    plt.savefig(output_path)
    plt.close()

def main():
    os.makedirs("graficos", exist_ok=True)
    archivos = [
        "logs/recovery_results_1.2.csv",
        "logs/recovery_results_1.3-A.csv"
    ]

    df_total = pd.concat([cargar_y_preparar_datos(archivo) for archivo in archivos], ignore_index=True)
    df_agg = agrupar_datos(df_total)
    graficar(df_agg, "graficos/precision_vs_ruido.png")

if __name__ == "__main__":
    main()
