import sys
sys.path.append("src")

from Hopfield_net import HopfieldNet
import random

def generate_random_pattern(n: int) -> list[int]:
    """Genera un patrón binario aleatorio de longitud n con valores -1 o 1."""
    return [random.choice([-1, 1]) for _ in range(n)]

def main():
    n_units = 128
    red = HopfieldNet(n_units)

    # Paso 1: Generar patrones y entrenar
    patrones = [generate_random_pattern(n_units) for _ in range(5)]
    red.train(patrones)

    # Paso 2: Seleccionamos uno para probar
    original = patrones[2]
    print("\nPatrón original:")
    print(original)

    # Paso 3: Añadimos ruido
    ruido = red.add_noise(original, noise_level=0.4)
    print("\nPatrón con ruido (40%):")
    print(ruido)

    # Paso 4: Recuperamos
    recuperado = red.recover(ruido, max_steps=1000)
    print("\nPatrón recuperado:")
    print(recuperado)

    # Paso 5: Evaluamos
    aciertos = sum(1 for a, b in zip(original, recuperado) if a == b)
    print(f"\nCoincidencias exactas: {aciertos}/{n_units} ({(aciertos/n_units)*100:.2f}%)")

if __name__ == "__main__":
    main()
