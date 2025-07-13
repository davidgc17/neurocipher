import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from symmetric_encrypt import generate_key, encrypt_message, decrypt_message

print("DEMO DE CIFRADO SIMÉTRICO CON FERNET")

#1.generar clave
key=generate_key()
print("clave generada:")
print(key.decode(), "\n")

#2. introducir mensaje
message = input("Introduce un mensaje a cifrar: ")

#3. cifrar
encrypted = encrypt_message(key, message)
print("\n Mensaje cifrado:")
print(encrypted.decode())

#4. descifrar
decrypted = decrypt_message(key, encrypted)
print("\n Mensaje descifrado:")
print(decrypted)