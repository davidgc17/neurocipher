import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from symmetric_encrypt import generate_key, encrypt_message, decrypt_message
from Hopfield_net import bytes_to_hopfield_pattern, hopfield_pattern_to_bytes, HopfieldNet

# 1. Generar clave original (32 bytes base64 para Fernet)
key_original = generate_key()

# 2. Cifrar un mensaje de prueba
mensaje = "Este mensaje es muy sensible"
ciphertext = encrypt_message(key_original, mensaje)

# 3. Convertir clave a patrón Hopfield y entrenar red
patron = bytes_to_hopfield_pattern(key_original)
net = HopfieldNet(n_units=len(patron))
net.train([patron])  # sin ruido, entrenamiento directo

# 4. Recuperar el patrón SIN aplicar ruido
recuperado = net.recover(patron)

# 5. Convertir el patrón recuperado a clave en bytes
key_recuperada = hopfield_pattern_to_bytes(recuperado)

# 6. Intentar descifrado con la clave recuperada
try:
    mensaje_descifrado = decrypt_message(key_recuperada, ciphertext)
except Exception as e:
    mensaje_descifrado = None
    print(f"❌ ERROR al descifrar: {e}")

# 7. Verificar si el mensaje coincide
if mensaje_descifrado == mensaje:
    print("✅ La clave Fernet fue correctamente preservada al pasar por la red Hopfield.")
else:
    print("❌ ERROR: El mensaje no pudo descifrarse tras pasar la clave por la red.")
    print(f"Mensaje original:   {mensaje}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")
