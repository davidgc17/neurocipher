import numpy as np
import random

class HopfieldNet:
    def __init__(self, n_units: int):
        """
        Inicializa una red de Hopfield con n unidades (neuronas).
        La matriz de pesos se inicializa a ceros.

        Args:
            n_units (int): Número de bits por patrón (ej. 128).
        """
        self.n = n_units
        self.weights = np.zeros((n_units, n_units))

    def train(self, patterns: list[list[int]]):
        """
        Entrena la red con una lista de patrones binarios usando la regla de Hebb.
        
        Cada patrón debe ser una lista de -1 y 1, de longitud igual a n_units.

        Args:
            patterns (list of list of int): Patrones a memorizar.
        """
        self.weights = np.zeros((self.n, self.n))  # Reset por si hay entrenamiento anterior

        for p in patterns:
            x = np.array(p)
            self.weights += np.outer(x, x)  # Producto exterior: w_ij = x_i * x_j

        # Eliminar autoconexiones
        np.fill_diagonal(self.weights, 0)
        # Normalización opcional
        self.weights /= self.n

    def recover(self, pattern: list[int], max_steps=100) -> list[int]:
        """
        Recupera un patrón a partir de una entrada posiblemente ruidosa.
        Usa actualización asincrónica.

        Args:
            pattern (list[int]): Patrón ruidoso (valores -1 y 1).
            max_steps (int): Número máximo de iteraciones.

        Returns:
            list[int]: Patrón recuperado.
        """
        state = np.array(pattern)
        
        for _ in range(max_steps):
            i = random.randint(0, self.n - 1)  # Neurona aleatoria
            net_input = np.dot(self.weights[i], state)
            state[i] = 1 if net_input >= 0 else -1  # Función de activación binaria

        return state.tolist()

    def add_noise(self, pattern: list[int], noise_level: float) -> list[int]:
        """
        Aplica ruido a un patrón, invirtiendo aleatoriamente una fracción de bits.

        Args:
            pattern (list[int]): Patrón original.
            noise_level (float): Fracción (0-1) de bits a alterar.

        Returns:
            list[int]: Patrón con ruido.
        """
        noisy = pattern[:]
        n_flips = int(len(pattern) * noise_level)
        indices = random.sample(range(len(pattern)), n_flips)
        for i in indices:
            noisy[i] *= -1
        return noisy

