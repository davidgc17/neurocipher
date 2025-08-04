
"""
Módulo para gestión segura de claves binarias:
- Asociar claves a un ID o alias
- Cifrar claves antes de almacenarlas
- Guardar y cargar desde archivo (JSON cifrado o binario)
- Recuperar claves y preparar para la red Hopfield
"""

from typing import Dict, List
from src.secure_key_utils import (
    generate_secure_key_bytes,
    bytes_to_bit_list,
    bit_list_to_bytes
)
import json
import os



# 1. Crear entrada de clave con ID asociado


def create_key_entry(key_id: str, length: int = 128) -> Dict:
    """
    Crea una entrada de clave con ID asociado.
    Genera la clave, la convierte a lista de bits, y empaqueta todo.

    :param key_id: Alias o identificador de la clave
    :param length: Longitud de la clave en bits
    :return: Diccionario con campos 'id', 'key_bytes', 'bit_list'
    """
    key_bytes = generate_secure_key_bytes(length)
    key_bits = bytes_to_bit_list(key_bytes)

    return {
        "id": key_id,
        "key_bytes": key_bytes,
        "bit_list": key_bits
    }


# 2. Listar IDs de una colección de claves


def list_key_ids(entries: List[Dict]) -> List[str]:
    """
    Extrae los IDs de una lista de claves.

    :param entries: Lista de entradas de clave
    :return: Lista de IDs (strings)
    """
    return [entry["id"] for entry in entries]



# 3. (Futuro) Cifrar una clave antes de guardarla


from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def encrypt_key_rsa(key_bytes: bytes, public_key: RSAPublicKey) -> bytes:
    """
    Cifra una clave binaria usando RSA con padding OAEP.

    :param key_bytes: Clave binaria en formato bytes (por ejemplo, 16 bytes = 128 bits)
    :param public_key: Clave pública RSA (objeto RSAPublicKey)
    :return: Clave cifrada como bytes
    """
    encrypted = public_key.encrypt(
        key_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


def decrypt_key_rsa(encrypted_bytes: bytes, private_key: RSAPrivateKey) -> bytes:
    """
    Descifra una clave binaria cifrada con RSA + OAEP.

    :param encrypted_bytes: Clave cifrada en formato bytes
    :param private_key: Clave privada RSA (objeto RSAPrivateKey)
    :return: Clave original en formato bytes
    """
    decrypted = private_key.decrypt(
        encrypted_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted





# 4. (Futuro) Guardar y cargar desde archivo


def save_keys_to_file(entries: List[Dict], filename: str):
    """
    Guarda una lista de claves (con ID y clave cifrada) en un archivo JSON estructurado.
    Convierte los bytes cifrados a hexadecimal para su serialización.

    :param entries: Lista de diccionarios con campos 'id' y 'key_bytes' (cifrados)
    :param filename: Nombre del archivo de salida (.json)
    """
    data = []

    for entry in entries:
        if not isinstance(entry.get("key_bytes"), bytes):
            raise ValueError(f"Entrada inválida: 'key_bytes' debe ser bytes")

        data.append({
            "id": entry["id"],
            "key_cifrada": entry["key_bytes"].hex(),
            "cifrado": "RSA-OAEP",
            "longitud_bits": len(entry["bit_list"])
        })
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_keys_from_file(filename: str) -> List[Dict]:
    """
    Carga las claves cifradas desde un archivo JSON.

    :param filename: Ruta del archivo JSON.
    :return: Lista de entradas (cada una con campos como 'id', 'key_cifrada', etc.).
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No se encontró el archivo: {filename}")

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def find_key_by_id(entries: List[Dict], alias: str) -> Dict:
    """
    Busca una entrada por su ID (alias) en la lista de claves cargadas.

    :param entries: Lista de entradas cargadas desde JSON.
    :param alias: Alias a buscar.
    :return: Entrada correspondiente al alias.
    :raises: ValueError si no se encuentra el alias.
    """
    for entry in entries:
        if entry.get("id") == alias:
            return entry
    raise ValueError(f"No se encontró ninguna clave con el alias '{alias}'")


# 5. (Futuro) Validar una clave recuperada con Hopfield


def validate_recovered_key(original_bits: List[int], recovered_bits: List[int]) -> float:
    """
    Compara dos claves en forma de listas de bits y calcula el % de coincidencia.

    :return: Porcentaje de coincidencia (0.0 - 100.0)
    """
    pass
