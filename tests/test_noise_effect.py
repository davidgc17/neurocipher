import sys, os
import random
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Hopfield_net import HopfieldNet
from src.Hopfield_net import bytes_to_hopfield_pattern, hopfield_pattern_to_bytes

# Clave base (ficticia o real)
original_key = bytes.fromhex("93b9d114d0eecab2a938f7ab0cf21e57")
pattern = bytes_to_hopfield_pattern(original_key)

# Crea red y entrena con la clave
net = HopfieldNet(n_units=len(pattern))
net.train([pattern])

# Recorremos diferentes niveles de ruido
for noise_level in np.arange(0.00, 0.75, 0.05):
    noisy = net.add_noise(pattern, noise_level)
    recovered = net.recover(noisy, max_steps=100)
    recovered_bytes = hopfield_pattern_to_bytes(recovered)

    # Estadísticas
    diff = net.bit_difference(pattern, noisy)
    recovery_exact = recovered_bytes == original_key
    accuracy = 100 * sum(b1 == b2 for b1, b2 in zip(original_key, recovered_bytes)) / len(original_key)

    print(f"\nRuido solicitado: {noise_level:.2f}")
    print(f"Bits diferentes aplicados: {diff} / {len(pattern)} ({100 * diff / len(pattern):.2f}%)")
    print(f"Recuperación exacta: {recovery_exact}")
    print(f"Precisión byte a byte: {accuracy:.2f}%")
