import hashlib
import random


class Point:
    def __init__(self, x, y, curve, is_infinity=False):
        self.x = x
        self.y = y
        self.curve = curve
        self.is_infinity = is_infinity

    def __eq__(self, other):
        if self.is_infinity and other.is_infinity:
            return True
        if self.is_infinity or other.is_infinity:
            return False
        return self.x == other.x and self.y == other.y and self.curve == other.curve

    def __neg__(self):
        if self.is_infinity:
            return self
        return Point(self.x, (-self.y) % self.curve.p, self.curve)

    def __str__(self):
        if self.is_infinity:
            return "Point(infinity)"
        return f"Point({self.x}, {self.y})"

class Curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, point):
        if point.is_infinity:
            return True
        lhs = (point.y * point.y) % self.p
        rhs = (point.x * point.x * point.x + self.a * point.x + self.b) % self.p
        return lhs == rhs

    def point_add(self, P, Q):
        """
        Suma dos puntos P y Q sobre la curva usando la operación de grupo.

        Args:
            P (Point): Primer punto.
            Q (Point): Segundo punto.

        Returns:
            Point: Resultado de P + Q.
        """
        # Casos especiales:
        if P.is_infinity:
            return Q
        if Q.is_infinity:
            return P
        if Q == -P:
            # Resultado es el punto en el infinito (identidad)
            return Point(None, None, self, True)

        if P == Q:
            # Suma punto consigo mismo (doble)
            numerator = (3 * P.x * P.x + self.a) % self.p
            denominator = modinv(2 * P.y, self.p)
            s = (numerator * denominator) % self.p
        else:
            # Suma puntos diferentes
            numerator = (Q.y - P.y) % self.p
            denominator = modinv((Q.x - P.x) % self.p, self.p)
            s = (numerator * denominator) % self.p

        x_r = (s * s - P.x - Q.x) % self.p
        y_r = (s * (P.x - x_r) - P.y) % self.p

        return Point(x_r, y_r, self)
    

    


    def scalar_mult(self, k, P):
        """
        Multiplicación escalar: calcula k * P usando suma repetida (doble y suma).

        Args:
            k (int): Escalar.
            P (Point): Punto de la curva.

        Returns:
            Point: Resultado de k * P.
        """
        R = Point(None, None, self, True)  # Punto en infinito (identidad)
        addend = P

        while k > 0:
            if k & 1:
                R = self.point_add(R, addend)
            addend = self.point_add(addend, addend)
            k >>= 1
        return R
    

    def generate_keypair(self, G, n):
        """
        Genera un par de claves ECC (privada y pública).
        """
        
        d = random.randrange(1, n)
        Q = self.scalar_mult(d, G)
        return d, Q
    



def modinv(a, p):
    # Inverso modular usando Euclides extendido
    if a == 0:
        raise ZeroDivisionError('No existe inverso modular de 0')
    lm, hm = 1, 0
    low, high = a % p, p
    while low > 1:
        r = high // low
        nm = hm - lm * r
        new = high - low * r
        hm, lm = lm, nm
        high, low = low, new
    return lm % p


def order_of_point(curve, G):
    count = 1
    point = G
    while True:
        point = curve.point_add(point, G)
        count += 1
        if point.is_infinity:
            return count


def ecdsa_sign(curve, private_key, G, n, message):
    """
    Genera una firma ECDSA para un mensaje dado.

    Args:
        curve (Curve): Objeto curva elíptica.
        private_key (int): Clave privada d.
        G (Point): Punto generador de la curva.
        n (int): Orden del grupo.
        message (str): Mensaje a firmar.

    Returns:
        (int, int): Tupla (r, s) que representa la firma.
    """
    # 1. Hash del mensaje con SHA-256 y convertir a entero
    e = int(hashlib.sha256(message.encode()).hexdigest(), 16)

    while True:
        # 2. Elegir nonce aleatorio k
        k = random.randrange(1, n)
        # 3. Calcular punto R = k*G
        R = curve.scalar_mult(k, G)
        r = R.x % n
        if r == 0:
            continue

        # 4. Calcular inverso modular de k
        k_inv = modinv(k, n)
        # 5. Calcular s = k^{-1} * (e + d*r) mod n
        s = (k_inv * (e + private_key * r)) % n
        if s == 0:
            continue

        return (r, s)

def ecdsa_verify(curve, public_key, G, n, message, signature):
    """
    Verifica una firma ECDSA para un mensaje dado.

    Args:
        curve (Curve): Objeto curva elíptica.
        public_key (Point): Clave pública Q = dG.
        G (Point): Punto generador de la curva.
        n (int): Orden del grupo.
        message (str): Mensaje firmado.
        signature (tuple): Tupla (r, s) con la firma.

    Returns:
        bool: True si la firma es válida, False en caso contrario.
    """
    r, s = signature
    if not (1 <= r < n and 1 <= s < n):
        return False

    e = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    w = modinv(s, n)
    u1 = (e * w) % n
    u2 = (r * w) % n

    # Calcular el punto X = u1*G + u2*Q
    point1 = curve.scalar_mult(u1, G)
    point2 = curve.scalar_mult(u2, public_key)
    X = curve.point_add(point1, point2)

    if X.is_infinity:
        return False

    return (X.x % n) == r
