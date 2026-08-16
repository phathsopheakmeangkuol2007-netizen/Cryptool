"""
Hash utilities for generating and comparing hashes
"""
import hashlib

def hash_data(data, algorithm):
    """
    Generate hash of data using specified algorithm
    
    Args:
        data (bytes): Data to hash
        algorithm (str): Hash algorithm (md5, sha1, sha256, sha512)
    
    Returns:
        str: Hexadecimal hash digest
    """
    if algorithm == 'md5':
        return hashlib.md5(data).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(data).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(data).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(data).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
