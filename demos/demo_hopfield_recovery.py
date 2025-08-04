import sys
import os
import numpy as np

sys.path.append(os.path.abspath("."))

from src.Hopfield_net import HopfieldNet, bytes_to_hopfield_pattern, hopfield_pattern_to_bytes
from src.secure_key_utils import generate_secure_key_bytes
from src.hopfield_logger import log_recovery_result

# Parámetros
annealing_start = 0.3
noise_levels = [round(v, 2) for v in np.arange(0.25, 0.55, 0.05)]
repetitions_list = [1, 2, 3, 5, 7, 10]
chunk_sizes = [1, 4, 8, 16, 32]

# Iterar combinaciones
for repetitions in repetitions_list:
    for chunk_size in chunk_sizes:
        print(f"\n== Probando rep={repetitions}, chunk_size={chunk_size} ==")

        # 1. Generar 3 claves distintas
        original_keys = [generate_secure_key_bytes(128) for _ in range(3)]
        patterns = [bytes_to_hopfield_pattern(key) for key in original_keys]

        # 2. Inicializar red, entrenar y annealing
        net = HopfieldNet(n_units=128)
        net.train(patterns, repetitions=repetitions)
        net.pretrain_with_annealing(patterns, start_noise=annealing_start, steps=10)

        # 3. Probar recuperación para cada patrón con ruido
        for idx, (original_key, pattern) in enumerate(zip(original_keys, patterns)):
            for noise_level in noise_levels:
                noisy = net.add_noise(pattern, noise_level)
                recovered = net.recover(noisy, chunk_size=chunk_size)
                recovered_bytes = hopfield_pattern_to_bytes(recovered)

                exact = original_key == recovered_bytes
                bits1 = ''.join(f"{b:08b}" for b in original_key)
                bits2 = ''.join(f"{b:08b}" for b in recovered_bytes)
                matches = sum(b1 == b2 for b1, b2 in zip(bits1, bits2))
                precision = 100 * matches / len(bits1)

                print(f"Clave {idx+1} | rep={repetitions} | chunk={chunk_size} | Ruido: {noise_level:.2f} | Exacta: {exact} | Precisión: {precision:.2f}%")

                log_recovery_result(
                    original_bytes=original_key,
                    recovered_bytes=recovered_bytes,
                    noise_level=noise_level,
                    version="1.3-A",
                    annealing_start=annealing_start,
                    annealing_steps=10,
                    pattern_id=f"key_{idx+1}",
                    bit_diff=len(bits1) - matches,
                    repetitions=repetitions,
                    chunk_size=chunk_size
                )
