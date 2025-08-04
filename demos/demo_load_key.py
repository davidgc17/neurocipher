import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.secure_key_manager import load_keys_from_file

# Ruta del archivo
input_path = os.path.abspath("keys/claves_guardadas.json")

# Cargar claves cifradas
try:
    entries = load_keys_from_file(input_path)
    print(f" Se han cargado {len(entries)} entradas.\n")

    for entry in entries:
        print(f"🔹 Alias: {entry['id']}")
        print(f"   Cifrado: {entry['cifrado']}")
        print(f"   Longitud: {entry['longitud_bits']} bits")
        print(f"   Clave cifrada (hex): {entry['key_cifrada'][:60]}...\n")

except Exception as e:
    print(f" Error al cargar: {e}")
