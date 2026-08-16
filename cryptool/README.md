# cryptool - Command-Line Cryptography Toolkit

A comprehensive command-line toolkit for cryptographic operations including encryption/decryption, classic ciphers, hashing, and password strength checking.

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required dependencies:
   ```bash
   pip install cryptography
   ```
3. Save the cryptool directory to your preferred location
4. You can run the tool directly from the directory or install it globally

## Usage

### Encryption and Decryption

Encrypt/decrypt text or files using AES-256-CBC with PBKDF2 key derivation.

**Encrypt a file:**
```bash
cryptool encrypt --file secret.txt --password mypass --output secret.txt.enc
```

**Encrypt text:**
```bash
cryptool encrypt --text "Hello World" --password mypass
```

**Decrypt a file:**
```bash
cryptool decrypt --file secret.txt.enc --password mypass --output decrypted.txt
```

**Decrypt text:**
```bash
cryptool decrypt --text <encrypted_bytes> --password mypass
```

### Classic Ciphers

Implementations of Caesar, Vigenère, and ROT13 ciphers for educational purposes.

**Caesar Cipher:**
```bash
# Encode
cryptool classic caesar --encode --text "hello" --shift 3

# Decode
cryptool classic caesar --decode --text "khoor" --shift 3
```

**Vigenère Cipher:**
```bash
# Encode
cryptool classic vigenere --encode --text "hello" --key "key"

# Decode
cryptool classic vigenere --decode --text "riijv" --key "key"
```

**ROT13:**
```bash
# Encode/Decode (ROT13 is its own inverse)
cryptool classic rot13 --encode --text "hello"
cryptool classic rot13 --decode --text "uryyb"
```

### Hashing

Generate hashes of text or files using various algorithms, and verify file integrity.

**Generate file hash:**
```bash
cryptool hash --file document.pdf --algo sha256
```

**Generate text hash:**
```bash
cryptool hash --text "Hello World" --algo md5
```

**Verify file integrity:**
```bash
cryptool hash --file document.pdf --algo sha256 --compare <expected_hash>
```

Supported algorithms: md5, sha1, sha256, sha512

### Password Strength Checking

Check password strength based on length, character variety, and common password dictionary.

**Check password:**
```bash
cryptool checkpw --password "test123"
```

**Check against common passwords:**
```bash
cryptool checkpw --password "password123" --common
```

## Examples

Here are some practical examples of how to use cryptool:

1. **Securely encrypt a sensitive file:**
   ```bash
   cryptool encrypt --file wallet.dat --password "MyStr0ngP@ssw0rd!" --output wallet.dat.enc
   ```

2. **Send an encrypted message using a classic cipher (for fun):**
   ```bash
   cryptool classic vigenere --encode --text "Meet me at midnight" --key "secret"
   ```

3. **Verify a downloaded file hasn't been corrupted:**
   ```bash
   cryptool hash --file linux-5.15.tar.xz --algo sha512 --compare <official_hash>
   ```

4. **Check if your password is strong enough:**
   ```bash
   cryptool checkpw --password "CorrectHorseBatteryStaple42!"
   ```

## How It Works

### Encryption
- Uses AES-256-CBC encryption
- Password is converted to a key using PBKDF2 with SHA-256, 100,000 iterations, and a random salt
- Each encryption uses a different random salt and initialization vector (IV)
- Output format: salt (16 bytes) + IV (16 bytes) + ciphertext

### Classic Ciphers
- **Caesar**: Shifts each letter by a fixed number
- **Vigenère**: Uses a keyword to determine different shifts for each letter
- **ROT13**: Special case of Caesar with shift of 13 (self-inverse)

### Hashing
- Uses Python's built-in hashlib library
- Supports MD5, SHA-1, SHA-256, and SHA-512 algorithms

### Password Strength
- Scores based on length (0-4 points), character variety (0-4 points)
- Checks against dictionary of common passwords
- Provides feedback on how to improve password strength
- Estimates crack time based on score

## Security Notes

1. The encryption implementation uses industry-standard AES-256 with proper key derivation
2. Never forget your password - there is no way to recover encrypted data without it
3. Classic ciphers are provided for educational purposes only - they are not secure for real protection
4. For maximum security, use long, random passwords with high entropy
5. The tool does not store any of your passwords or data

## Requirements

- Python 3.6+
- cryptography library (`pip install cryptography`)

## License

MIT License - feel free to modify and distribute as needed.
