import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.secure_key_manager import load_keys_from_file, find_key_by_id

input_path = os.path.abspath("keys/claves_guardadas.json")

try:
    entries = load_keys_from_file(input_path)

    alias = "clave_demo"  # Puedes cambiarlo por cualquier otro alias que tengas guardado
    entry = find_key_by_id(entries, alias)

    print("Clave encontrada:")
    print(f"Alias: {entry['id']}")
    print(f"Cifrado: {entry['cifrado']}")
    print(f"Clave cifrada (hex): {entry['key_cifrada'][:60]}...")

except Exception as e:
    print(f"Error: {e}")
