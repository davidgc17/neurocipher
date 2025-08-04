import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.secure_key_utils import generate_secure_key_bytes
from src.asymmetric_crypt import generate_rsa_keypair
from src.secure_key_manager import encrypt_key_rsa, create_key_entry, save_keys_to_file
import json




# Generar par de claves RSA
private_key, public_key = generate_rsa_keypair()

# Crear entrada de clave con alias
entry = create_key_entry("clave_demo")  # 128 bits

# Cifrar la clave con RSA
entry["key_bytes"] = encrypt_key_rsa(entry["key_bytes"], public_key)

# Guardar en archivo JSON
output_path = os.path.abspath("keys/claves_guardadas.json")
save_keys_to_file([entry], output_path)

print(f" Clave cifrada guardada en:\n{output_path}")
print(" Archivo existe:", os.path.exists(output_path))

