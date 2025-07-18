import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.asymmetric_crypt import (
    generate_rsa_keypair,
    encrypt_message_rsa,
    decrypt_message_rsa
)

print("\n--- DEMO DE CIFRADO Y DESCIFRADO RSA ---\n")

# Paso 1: generar claves
private_key, public_key = generate_rsa_keypair()
print("Claves RSA generadas (2048 bits)")

# Paso 2: mensaje a cifrar
mensaje_original = "Este mensaje será cifrado con RSA moderno."
print("\nMensaje original:")
print(mensaje_original)

# Paso 3: cifrado
cifrado = encrypt_message_rsa(mensaje_original, public_key)
print("\nMensaje cifrado (hexadecimal):")
print(cifrado.hex())

# Paso 4: descifrado
descifrado = decrypt_message_rsa(cifrado, private_key)
print("\nMensaje descifrado:")
print(descifrado)
