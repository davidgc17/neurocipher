import unittest
import sys
import os

# Añadimos src/ al path para que funcione la importación
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from rsa_basic import gcd, modinv, generate_keys

class TestRSA(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_modinv(self):
        self.assertEqual(modinv(3, 11), 4)

    def test_generate_keys(self):
        public, private = generate_keys(bits=16)
        self.assertIsInstance(public, tuple)
        self.assertIsInstance(private, tuple)

if __name__ == '__main__':
    unittest.main()
