# secure_key_utils.py

import os
from typing import List

def generate_secure_key_bytes(length: int = 128) -> bytes:
    """
    Genera una clave aleatoria segura de longitud 'length' bits (por defecto 128).
    Devuelve la clave como objeto bytes.

    :param length: Longitud de la clave en bits (múltiplo de 8).
    :return: Clave generada como bytes.
    """
    if length % 8 != 0:
        raise ValueError("La longitud debe ser múltiplo de 8 bits.")
    byte_length = length // 8
    return os.urandom(byte_length)


def bytes_to_bit_list(b: bytes) -> List[int]:
    """
    Convierte una clave en bytes a una lista de bits (0s y 1s).

    :param b: Clave en formato bytes.
    :return: Lista de bits (valores 0 o 1).
    """
    return [int(bit) for byte in b for bit in f'{byte:08b}']


def bit_list_to_bytes(bits: List[int]) -> bytes:
    """
    Convierte una lista de bits (0s y 1s) a bytes.

    :param bits: Lista de bits (debe tener longitud múltiplo de 8).
    :return: Objeto bytes reconstruido.
    """
    if len(bits) % 8 != 0:
        raise ValueError("La lista de bits debe tener una longitud múltiplo de 8.")
    byte_chunks = [''.join(str(bit) for bit in bits[i:i+8]) for i in range(0, len(bits), 8)]
    return bytes([int(chunk, 2) for chunk in byte_chunks])


def bytes_to_binstr(b: bytes) -> str:
    """
    Convierte bytes a un string binario (solo 0s y 1s).

    :param b: Clave en formato bytes.
    :return: Cadena binaria en texto.
    """
    return ''.join(f'{byte:08b}' for byte in b)


def binstr_to_bytes(s: str) -> bytes:
    """
    Convierte una cadena binaria de texto a bytes.

    :param s: String binario (longitud múltiplo de 8).
    :return: Objeto bytes.
    """
    if len(s) % 8 != 0:
        raise ValueError("La cadena binaria debe tener una longitud múltiplo de 8.")
    return bytes([int(s[i:i+8], 2) for i in range(0, len(s), 8)])


from cryptography.hazmat.primitives.serialization import load_pem_private_key

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

def save_rsa_private_key(private_key: RSAPrivateKey, filepath: str, password: bytes = None) -> None:
    """
    Guarda una clave privada RSA en un archivo .pem.

    :param private_key: Clave privada RSA a guardar
    :param filepath: Ruta de destino del archivo
    :param password: Contraseña opcional para cifrado (en bytes)
    """
    encryption_algorithm = (
        serialization.BestAvailableEncryption(password)
        if password else
        serialization.NoEncryption()
    )

    pem_data = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )

    with open(filepath, "wb") as f:
        f.write(pem_data)


def load_rsa_private_key(filepath: str, password: bytes = None) -> RSAPrivateKey:
    """
    Carga una clave privada RSA desde archivo .pem.

    :param filepath: Ruta al archivo .pem
    :param password: Contraseña si está cifrada (en bytes)
    :return: Clave privada RSA (RSAPrivateKey)
    """
    with open(filepath, "rb") as f:
        pem_data = f.read()

    private_key = load_pem_private_key(pem_data, password=password)
    return private_key
