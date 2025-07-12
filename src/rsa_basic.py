from Crypto.Util.number import getPrime
import random




def gcd(a: int, b: int) -> int:
#Calcula el máximo común divisor (MCD) de dos números a y b usando el algoritmo de Euclides.#

    while b != 0:
        a, b = b, a % b
    return a
def modinv(a: int, m: int) -> int:
#Calcula el inverso modular de a módulo m usando el algoritmo extendido de Euclides. Retorna x tq (a*x) % m == 1. Lanza una excepcion si el inverso no existe (cuando gcd(a,m) != 1).#
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a//m 
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if a != 1:
        raise ValueError("No existe inverso modular para los valores elegidos")
    return x1 % m0

def generate_keys(bits: int = 16):
#genera un par de claves RSA(pública y privada).

#paso 1: elegir primos p y q
    p = getPrime(bits)
    q = getPrime(bits)
    while q == p :
        q = getPrime(bits)

#paso 2:calcular n y phi(n)
    n = p * q
    phi = (p-1)*(q-1)

#paso 3: elegir e tq 1<e<phi y gcd(e,phi)=1
    e = random.randrange(2,phi)
    while gcd(e,phi) !=1:
        e=random.randrange(2,phi)

#paso 4: calcular d = e^(-1) mod phi
    d = modinv(e, phi)

#Clave pública: (e,n) | clave privada: (d,n)
    return (e,n), (d,n)

def encrypt_message(message: str, public_key: tuple) -> list[int]:
    e, n = public_key
    encrypted = []

    for char in message:
        #convertimos el carácter a su valor ASCII (entero)
        m=ord(char)
        #Aplicamos cifrado RSA: c = m^e mod n
        if m >= n:
            raise ValueError(f"El carácter '{char}' con valor ASCII {m} es demasiado grande para el módulo n={n}.")
        c = pow(m,e,n)
        encrypted.append(c)
    
    return encrypted

def decrypt_message(ciphertext: list[int], private_key: tuple) -> str:
    d, n = private_key
    decrypted = ""

    for c in ciphertext:
        if c >= n:
            raise ValueError(f"El valor cifrado {c} no puede descifrarse: debe ser menor que n={n}")
        # Aplicamos descifrado RSA: m = c^d mod n
        m = pow(c, d, n)
        decrypted += chr(m)

    return decrypted

    
if __name__ == "__main__":
    print("gcd(48, 18) =", gcd(48, 18))  # Debe devolver 6
    print("gcd(7, 3) =", gcd(7, 3))      # Debe devolver 1

    print("modinv(3,11) =", modinv(3, 11)) # Debe devolver 4
    print("modinv(10,17) =", modinv(10,17)) #Debe devolver 12

    public_key, private_key = generate_keys(16)
    print("Clave pública:", public_key)
    print("Clave privada:", private_key)

    mensaje = "Hola"
    cifrado = encrypt_message(mensaje, public_key)
    print("Mensaje cifrado:", cifrado)

    descifrado = decrypt_message(cifrado, private_key)
    print("Mensaje descifrado:", descifrado)
