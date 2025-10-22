from cryptography.fernet import Fernet

def load_key():
    """Loads the key from the secret.key file"""
    return open("secret.key", "rb").read()

def decrypt_file(encrypted_filename, output_filename):
    """Decrypts an encrypted file"""
    key = load_key()
    f = Fernet(key)

    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data) 

    with open(output_filename, "wb") as file:
        file.write(decrypted_data)

    return output_filename