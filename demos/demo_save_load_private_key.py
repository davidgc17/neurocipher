import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.asymmetric_crypt import generate_rsa_keypair
from src.secure_key_utils import (
    save_rsa_private_key,
    load_rsa_private_key
)


# Ruta donde guardar la clave
output_path = os.path.abspath("keys/private_key.pem")

# Generar clave nueva
private_key, public_key = generate_rsa_keypair()

# Guardar sin cifrado
save_rsa_private_key(private_key, output_path)

# Cargar desde archivo
loaded_key = load_rsa_private_key(output_path)

# Verificación
assert private_key.private_numbers() == loaded_key.private_numbers(), " Las claves no coinciden"
print(" Clave privada cargada y verificada correctamente.")