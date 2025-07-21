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
        import random
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
