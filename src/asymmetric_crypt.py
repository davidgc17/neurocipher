from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes



def generate_rsa_keypair(key_size: int = 2048, public_exponent: int = 65537):
    """
    Genera un par de claves RSA seguras utilizando la librería cryptography.

    Args:
        key_size (int): Tamaño de la clave en bits (mínimo recomendado: 2048).
        public_exponent (int): Exponente público. Recomendado: 65537.

    Returns:
        tuple: (clave_privada, clave_pública) como objetos RSA.
    """
    private_key = rsa.generate_private_key(
        public_exponent=public_exponent,
        key_size=key_size
    )
    public_key = private_key.public_key()
    return private_key, public_key


def export_private_key_pem(private_key, password: bytes = None) -> bytes:
    """
    Serializa una clave privada en formato PEM.

    Args:
        private_key: Objeto RSAPrivateKey.
        password (bytes): Contraseña opcional para cifrar la clave.

    Returns:
        bytes: Clave privada codificada en PEM.
    """
    encryption = serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption
    )


def export_public_key_pem(public_key) -> bytes:
    """
    Serializa una clave pública en formato PEM.

    Args:
        public_key: Objeto RSAPublicKey.

    Returns:
        bytes: Clave pública codificada en PEM.
    """
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def encrypt_message_rsa(message: str, public_key) -> bytes:
    """
    Cifra un mensaje usando una clave pública RSA y padding OAEP.

    Args:
        message (str): Texto a cifrar.
        public_key: Objeto RSAPublicKey.

    Returns:
        bytes: Mensaje cifrado como bytes.
    """
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def decrypt_message_rsa(ciphertext: bytes, private_key) -> str:
    """
    Descifra un mensaje cifrado con RSA usando la clave privada correspondiente.

    Args:
        ciphertext (bytes): Mensaje cifrado.
        private_key: Objeto RSAPrivateKey.

    Returns:
        str: Texto plano descifrado.
    """
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()