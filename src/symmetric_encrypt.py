from cryptography.fernet import Fernet

def generate_key():
    # Generamos una clave simétrica segura para Fernet. Devuelve una clave en formato base64.
    return Fernet.generate_key()

def encrypt_message(key: bytes, message: str) -> bytes:
    # Ciframos el mensaje utilizando la clave proporcionada.
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key: bytes, token: bytes) -> str:
    # Desciframos el mensaje utilizando la clave proporcionada.
    f = Fernet(key)
    return f.decrypt(token).decode()

def encrypt_file(key: bytes, input_path: str, output_path: str) -> None:
    # Ciframos el contenido de un archivo de texto plano y guardamos el archivo cifrado.
    f = Fernet(key)
    with open(input_path, 'rb') as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key: bytes, input_path: str, output_path: str) -> None:
    # Desciframos el contenido de un archivo cifrado y guardamos el archivo de texto plano.
    f = Fernet(key)
    with open(input_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(output_path, 'wb') as file:
        file.write(decrypted_data)
