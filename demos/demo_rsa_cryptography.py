import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.asymmetric_crypt import (
    generate_rsa_keypair,
    export_private_key_pem,
    export_public_key_pem
)

# Asegurar que el directorio "keys/" existe
os.makedirs("keys", exist_ok=True)

# Generar las claves
private_key, public_key = generate_rsa_keypair()

# Exportar a formato PEM
private_pem = export_private_key_pem(private_key)
public_pem = export_public_key_pem(public_key)

# Guardar en archivos .pem
with open("keys/private_key.pem", "wb") as priv_file:
    priv_file.write(private_pem)

with open("keys/public_key.pem", "wb") as pub_file:
    pub_file.write(public_pem)

print("✅ Claves RSA generadas y guardadas en carpeta 'keys/'")
