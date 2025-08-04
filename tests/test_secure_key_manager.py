import unittest
from src.asymmetric_crypt import generate_rsa_keypair
from src.secure_key_utils import generate_secure_key_bytes
from src.secure_key_manager import encrypt_key_rsa, decrypt_key_rsa, create_key_entry, list_key_ids



class TestSecureKeyManager(unittest.TestCase):

    def test_create_key_entry(self):
        entry = create_key_entry("clave_demo", 128)
        self.assertEqual(entry["id"], "clave_demo")
        self.assertEqual(len(entry["bit_list"]), 128)
        self.assertEqual(len(entry["key_bytes"]), 16)



    def test_encrypt_decrypt_key_rsa(self):
        private_key, public_key = generate_rsa_keypair()
        original_key = generate_secure_key_bytes(128)
        encrypted_key = encrypt_key_rsa(original_key, public_key)
        decrypted_key = decrypt_key_rsa(encrypted_key, private_key)
    
        self.assertEqual(original_key, decrypted_key)


if __name__ == '__main__':
    unittest.main()
