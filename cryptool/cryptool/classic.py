"""
Classic ciphers for learning purposes
"""

def caesar_encode(text, shift):
    """Encode text using Caesar cipher"""
    result = []
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decode(text, shift):
    """Decode text using Caesar cipher"""
    return caesar_encode(text, -shift)

def vigenere_encode(text, key):
    """Encode text using Vigenère cipher"""
    result = []
    key_index = 0
    key = key.lower()
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - ord('a')
            result.append(chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decode(text, key):
    """Decode text using Vigenère cipher"""
    result = []
    key_index = 0
    key = key.lower()
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - ord('a')
            result.append(chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

def rot13_encode(text):
    """Encode text using ROT13 cipher"""
    return caesar_encode(text, 13)

def rot13_decode(text):
    """Decode text using ROT13 cipher"""
    return caesar_decode(text, 13)
