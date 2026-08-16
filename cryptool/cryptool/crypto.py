"""
Encryption and decryption module using AES with PBKDF2 key derivation
"""
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt(data, password):
    """
    Encrypt data using AES-256-CBC with PBKDF2 key derivation
    
    Args:
        data (bytes): Data to encrypt
        password (str): Password for encryption
    
    Returns:
        bytes: Encrypted data (salt + iv + ciphertext)
    """
    # Generate a random salt
    salt = os.urandom(16)
    
    # Derive key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    
    # Generate a random IV
    iv = os.urandom(16)
    
    # Encrypt data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad data to be multiple of block size (16 bytes for AES)
    padding_length = 16 - (len(data) % 16)
    padded_data = data + bytes([padding_length] * padding_length)
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return salt + iv + ciphertext
    return salt + iv + ciphertext

def decrypt(data, password):
    """
    Decrypt data using AES-256-CBC with PBKDF2 key derivation
    
    Args:
        data (bytes): Encrypted data (salt + iv + ciphertext)
        password (str): Password for decryption
    
    Returns:
        bytes: Decrypted data
    """
    # Extract salt, iv, and ciphertext
    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]
    
    # Derive key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    
    # Decrypt data
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove padding
    padding_length = padded_data[-1]
    data = padded_data[:-padding_length]
    
    return data
