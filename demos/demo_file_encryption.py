import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.symmetric_encrypt import generate_key, encrypt_file, decrypt_file


try:
    print("\nDEMO DE CIFRADO SIMÉTRICO DE ARCHIVOS CON FERNET")

    key = generate_key()
    print("\nClave generada:")
    print(key.decode())

    input_path = "data/mensaje_original.txt"
    encrypted_path = "data/mensaje_cifrado.txt"
    decrypted_path = "data/mensaje_descifrado.txt"

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(input_path):
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write("Este es un mensaje confidencial que será cifrado con Fernet.")

    print("\nArchivo original creado en:", input_path)

    encrypt_file(key, input_path, encrypted_path)
    print("\nArchivo cifrado guardado en:", encrypted_path)

    decrypt_file(key, encrypted_path, decrypted_path)
    print("\nArchivo descifrado guardado en:", decrypted_path)

    with open(decrypted_path, 'r', encoding='utf-8') as f:
        contenido = f.read()

    print("\nContenido del archivo descifrado:\n", contenido)

except Exception as e:
    print("\n[ERROR EN LA EJECUCIÓN]:", str(e))
