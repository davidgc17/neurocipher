import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.elliptic_curve import Curve, Point

def main():
    # Parámetros para la curva de prueba
    a = 2
    b = 3
    p = 97  # campo primo pequeño

    curve = Curve(a, b, p)

    # Punto generador (debe estar en la curva)
    G = Point(3, 6, curve)
    assert curve.is_on_curve(G), "G no está en la curva"

    # Orden pequeño para pruebas (valor arbitrario para demo)
    n = 5

    # Generar claves
    private_key, public_key = curve.generate_keypair(G, n)

    print(f"Clave privada (entero): {private_key}")
    print(f"Clave pública (punto): {public_key}")

if __name__ == "__main__":
    main()
