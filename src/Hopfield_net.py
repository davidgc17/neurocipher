import numpy as np
import random


def bytes_to_hopfield_pattern(key_bytes: bytes) -> list[int]:
    """
    Convierte una clave en bytes a un patrón binario {-1, 1} para redes de Hopfield.
    """
    bits = []
    for byte in key_bytes:
        for i in range(8):
            bit = (byte >> (7 - i)) & 1
            bits.append(1 if bit == 1 else -1)
    return bits


def hopfield_pattern_to_bytes(pattern: list[int]) -> bytes:
    """
    Convierte un patrón {-1, 1} de vuelta a clave en formato bytes.
    """
    if len(pattern) % 8 != 0:
        raise ValueError("La longitud del patrón debe ser múltiplo de 8.")

    byte_list = []
    for i in range(0, len(pattern), 8):
        byte = 0
        for j in range(8):
            bit = 1 if pattern[i + j] == 1 else 0
            byte = (byte << 1) | bit
        byte_list.append(byte)
    return bytes(byte_list)


class HopfieldNet:
    def __init__(self, n_units: int):
        self.n = n_units
        self.weights = np.zeros((n_units, n_units))

    def train(self, patterns: list[list[int]], repetitions: int = 1):
        """
        Entrena la red con una lista de patrones usando la regla de Hebb.
        Puedes repetir los patrones varias veces para reforzarlos.
        """
        self.weights = np.zeros((self.n, self.n))

        for _ in range(repetitions):
            for p in patterns:
                x = np.array(p)
                self.weights += np.outer(x, x)

        np.fill_diagonal(self.weights, 0)
        self.weights /= self.n

    def pretrain_with_annealing(self, patterns: list[list[int]], start_noise: float = 0.3, end_noise: float = 0.0, steps: int = 5):
        noise_levels = np.linspace(start_noise, end_noise, steps)
        all_variants = []

        for noise in noise_levels:
            for pattern in patterns:
                noisy = self.add_noise(pattern, noise)
                all_variants.append(noisy)

        self.train(all_variants)

    def recover(self, pattern: list[int], max_steps=100, chunk_size: int = 1) -> list[int]:
        """
        Recupera un patrón ruidoso usando actualización por bloques.
        """
        state = np.array(pattern)
        indices = np.arange(self.n)

        for _ in range(max_steps):
            np.random.shuffle(indices)
            for i in range(0, self.n, chunk_size):
                chunk = indices[i:i + chunk_size]
                net_input = np.dot(self.weights[chunk], state)
                state[chunk] = np.where(net_input >= 0, 1, -1)

        return state.tolist()

    def add_noise(self, pattern: list[int], noise_level: float) -> list[int]:
        noisy = pattern[:]
        n_flips = int(len(pattern) * noise_level)
        indices = random.sample(range(len(pattern)), n_flips)
        for i in indices:
            noisy[i] *= -1
        return noisy

    def bit_difference(self, p1: list[int], p2: list[int]) -> int:
        return sum(b1 != b2 for b1, b2 in zip(p1, p2))



