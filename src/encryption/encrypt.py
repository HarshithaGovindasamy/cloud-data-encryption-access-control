from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates a key and saves it into a file"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the secret.key file"""
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    """Encrypts a file using the loaded key"""
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    # Use a new filename for the encrypted data
    encrypted_filename = filename + ".encrypted"
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    return encrypted_filename