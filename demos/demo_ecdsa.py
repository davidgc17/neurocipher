import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.elliptic_curve import Curve, Point, ecdsa_sign, ecdsa_verify, order_of_point

def main():
    a = 2
    b = 3
    p = 97

    curve = Curve(a, b, p)

    G = Point(3, 6, curve)
    assert curve.is_on_curve(G), "G no está en la curva"

    n = order_of_point(curve, G)
    print(f"Orden de G: {n}")


    d, Q = curve.generate_keypair(G, n)
    print(f"Clave privada: {d}")
    print(f"Clave pública: {Q}")

    mensaje = "Mensaje de prueba"
    print(f"Mensaje: {mensaje}")

    firma = ecdsa_sign(curve, d, G, n, mensaje)
    print(f"Firma generada: {firma}")

    valido = ecdsa_verify(curve, Q, G, n, mensaje, firma)
    print(f"Verificación válida: {valido}")

if __name__ == "__main__":
    main()
