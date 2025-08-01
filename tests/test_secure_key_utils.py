# tests/test_secure_key_utils.py

import unittest
from src.secure_key_utils import (
    generate_secure_key_bytes,
    bytes_to_bit_list,
    bit_list_to_bytes,
    bytes_to_binstr,
    binstr_to_bytes
)

class TestSecureKeyUtils(unittest.TestCase):

    def test_bytes_to_bit_list_and_back(self):
        key_bytes = generate_secure_key_bytes(128)
        bits = bytes_to_bit_list(key_bytes)
        recovered_bytes = bit_list_to_bytes(bits)
        self.assertEqual(key_bytes, recovered_bytes, "Conversión bytes → bits → bytes fallida")

    def test_bytes_to_binstr_and_back(self):
        key_bytes = generate_secure_key_bytes(128)
        binstr = bytes_to_binstr(key_bytes)
        recovered_bytes = binstr_to_bytes(binstr)
        self.assertEqual(key_bytes, recovered_bytes, "Conversión bytes → string binario → bytes fallida")

    def test_bit_list_length(self):
        key_bytes = generate_secure_key_bytes(128)
        bits = bytes_to_bit_list(key_bytes)
        self.assertEqual(len(bits), 128, "La longitud de bits no es 128")

    def test_binstr_length(self):
        key_bytes = generate_secure_key_bytes(128)
        binstr = bytes_to_binstr(key_bytes)
        self.assertEqual(len(binstr), 128, "La longitud del string binario no es 128")


if __name__ == '__main__':
    unittest.main()
