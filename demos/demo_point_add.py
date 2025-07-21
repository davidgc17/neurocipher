import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.elliptic_curve import Curve, Point

def main():
    # Parámetros de una curva pequeña para pruebas (campo primo pequeño)
    a = 2
    b = 3
    p = 97  # Primo pequeño para ejemplo

    curve = Curve(a, b, p)

    # Dos puntos de prueba (asegúrate que están en la curva)
    P = Point(3, 6, curve)
    Q = Point(80, 10, curve)

    print(f"P: {P}")
    print(f"Q: {Q}")

    # Verificar que están en la curva
    assert curve.is_on_curve(P), "P no está en la curva"
    assert curve.is_on_curve(Q), "Q no está en la curva"

    # Sumar puntos
    R = curve.point_add(P, Q)

    print(f"P + Q = {R}")

if __name__ == "__main__":
    main()
