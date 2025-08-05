import csv
import os
from datetime import datetime

from datetime import datetime
from src.Hopfield_net import (
    HopfieldNet,
    bytes_to_hopfield_pattern,
    hopfield_pattern_to_bytes
)
from src.rsa_basic import generate_keys, encrypt_message as rsa_encrypt, decrypt_message as rsa_decrypt
from src.symmetric_encrypt import generate_key as generate_aes_key
from src.symmetric_encrypt import encrypt_message as aes_encrypt, decrypt_message as aes_decrypt


def run_secure_session(message: str, method: str = "AES", noise_level: float = 0.3) -> dict:
    """
    Cifra un mensaje con AES o RSA, guarda la clave en una red Hopfield,
    simula ruido, recupera la clave y descifra el mensaje.
    Entrenamiento combinado: pretraining + refuerzo del patrón limpio.
    """
    # ----- 1. Generar clave y cifrar -----
    if method.upper() == "AES":
        key_bytes = generate_aes_key()  # Fernet: 32 bytes
        encrypted = aes_encrypt(key_bytes, message)
        key_for_hopfield = key_bytes  # 256 bits

    elif method.upper() == "RSA":
        pub, priv = generate_keys(bits=16)
        encrypted = rsa_encrypt(message, pub)
        d, n = priv
        key_for_hopfield = d.to_bytes(16, 'big')  # 128 bits

    else:
        raise ValueError("Método no soportado: usa 'AES' o 'RSA'.")

    # ----- 2. Convertir clave a patrón binario {-1, 1} -----
    original_pattern = bytes_to_hopfield_pattern(key_for_hopfield)

    # ----- 3. Crear red Hopfield y entrenar -----
    net = HopfieldNet(n_units=len(original_pattern))

    # Preentrenamiento con ruido (annealing)
    net.pretrain_with_annealing(
        patterns=[original_pattern],
        start_noise=0.3,
        end_noise=0.0,
        steps=5
    )

    # Refuerzo del patrón limpio
    net.train([original_pattern], repetitions=3)

    # ----- 4. Aplicar ruido y recuperar -----
    noisy = net.add_noise(original_pattern, noise_level)
    recovered = net.recover(noisy, chunk_size=8)

    # ----- 5. Medir precisión -----
    bit_diff = net.bit_difference(original_pattern, recovered)
    accuracy = 1 - (bit_diff / len(original_pattern))
    recovered_ok = accuracy >= 0.95

    # ----- 6. Intentar descifrado -----
    try:
        recovered_bytes = hopfield_pattern_to_bytes(recovered)

        if method.upper() == "AES":
            decrypted = aes_decrypt(recovered_bytes, encrypted)
        else:
            recovered_d = int.from_bytes(recovered_bytes, 'big')
            recovered_priv = (recovered_d, n)
            decrypted = rsa_decrypt(encrypted, recovered_priv)
    except Exception:
        decrypted = None

    # ----- 7. Evaluar éxito -----
    success = decrypted == message
    print(f"[{datetime.now()}] Método: {method}, Ruido: {noise_level*100:.1f}%, Precisión: {accuracy*100:.2f}%, Éxito: {success}")

    return {
        "method": method,
        "noise": noise_level,
        "precision": accuracy,
        "recovered": recovered_ok,
        "success": success
    }


if __name__ == "__main__":
    mensajes = [
    "Mensaje 1: básico",
    "Mensaje 2: con acentos áéíóú",
    "Mensaje 3: más largo, con puntuación... ¿qué pasa si lo alargamos mucho más aún?",
    "Mensaje 4: números 1234567890",
    "Mensaje 5: símbolos $%&/()=?¡¿",
    "Mensaje 6: prueba final con mezcla ÁÑç<>~#@!"
]

    niveles_de_ruido = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    metodos = ["AES", "RSA"]

    output_path = "logs"
    os.makedirs(output_path, exist_ok=True)

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_path, f"experimentos_hopfield_{fecha}.csv")

    print("\n=== PRUEBAS EXTENDIDAS CON AES ===")
    for msg in mensajes:
        print(f"\n🔐 Mensaje: \"{msg}\"")
        for noise in niveles_de_ruido:
            run_secure_session(msg, method="AES", noise_level=noise)

    print("\n=== PRUEBAS EXTENDIDAS CON RSA ===")
    for msg in mensajes:
        print(f"\n🔐 Mensaje: \"{msg}\"")
        for noise in niveles_de_ruido:
            run_secure_session(msg, method="RSA", noise_level=noise)

# ==== CABECERA DEL CSV ====

with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "mensaje", "metodo", "ruido", "precision", "recuperado", "exito"])

    # ==== EJECUCIÓN DE TODAS LAS PRUEBAS ====
    for metodo in metodos:
        for mensaje in mensajes:
            for ruido in niveles_de_ruido:
                resultado = run_secure_session(mensaje, metodo, ruido)

                writer.writerow([
                    datetime.now().isoformat(),
                    mensaje,
                    resultado["method"],
                    resultado["noise"],
                    round(resultado["precision"] * 100, 2),
                    resultado["recovered"],
                    resultado["success"]
                ])

print(f"\n✅ Resultados guardados en: {output_file}")
