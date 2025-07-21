import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.elliptic_curve import Curve, Point

def main():
    # Parámetros de prueba
    a = 2
    b = 3
    p = 97

    curve = Curve(a, b, p)

    P = Point(3, 6, curve)
    print(f"P: {P}")

    # Escalar k
    k = 20
    R = curve.scalar_mult(k, P)

    print(f"{k} * P = {R}")

if __name__ == "__main__":
    main()
