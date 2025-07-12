from rsa_basic import generate_keys, encrypt_message, decrypt_message

def main():
    # Paso 1: Generar claves
    public_key, private_key = generate_keys(bits=16)
    print(f"Clave pública: {public_key}")
    print(f"Clave privada: {private_key}")

    # Paso 2: Mensaje a cifrar
    mensaje = "Hola RSA"
    print(f"\nMensaje original: {mensaje}")

    # Paso 3: Cifrar el mensaje
    cifrado = encrypt_message(mensaje, public_key)
    print(f"\nMensaje cifrado: {cifrado}")

    # Paso 4: Descifrar el mensaje
    descifrado = decrypt_message(cifrado, private_key)
    print(f"\nMensaje descifrado: {descifrado}")

if __name__ == "__main__":
    main()