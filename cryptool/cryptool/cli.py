#!/usr/bin/env python3
"""
cryptool - A command-line cryptography toolkit
"""

import argparse
import sys
from . import crypto, classic, hash_utils, password

def main():
    parser = argparse.ArgumentParser(
        description="cryptool - A command-line cryptography toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cryptool encrypt --file secret.txt --password mypass
  cryptool decrypt --file secret.txt.enc --password mypass
  cryptool classic caesar --encode "hello" --shift 3
  cryptool classic vigenere --decode "khoor" --key "key"
  cryptool hash --file document.pdf --algo sha256
  cryptool checkpw --password "test123"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt text or file')
    encrypt_parser.add_argument('--file', '-f', help='File to encrypt')
    encrypt_parser.add_argument('--text', '-t', help='Text to encrypt')
    encrypt_parser.add_argument('--password', '-p', required=True, help='Password for encryption')
    encrypt_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    # Decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt text or file')
    decrypt_parser.add_argument('--file', '-f', help='File to decrypt')
    decrypt_parser.add_argument('--text', '-t', help='Text to decrypt')
    decrypt_parser.add_argument('--password', '-p', required=True, help='Password for decryption')
    decrypt_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    # Classic command
    classic_parser = subparsers.add_parser('classic', help='Classic ciphers')
    classic_subparsers = classic_parser.add_subparsers(dest='cipher', help='Cipher type')
    
    # Caesar cipher
    caesar_parser = classic_subparsers.add_parser('caesar', help='Caesar cipher')
    caesar_parser.add_argument('--encode', action='store_true', help='Encode text')
    caesar_parser.add_argument('--decode', action='store_true', help='Decode text')
    caesar_parser.add_argument('--text', '-t', required=True, help='Text to process')
    caesar_parser.add_argument('--shift', '-s', type=int, required=True, help='Shift value')
    caesar_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    # Vigenère cipher
    vigenere_parser = classic_subparsers.add_parser('vigenere', help='Vigenère cipher')
    vigenere_parser.add_argument('--encode', action='store_true', help='Encode text')
    vigenere_parser.add_argument('--decode', action='store_true', help='Decode text')
    vigenere_parser.add_argument('--text', '-t', required=True, help='Text to process')
    vigenere_parser.add_argument('--key', '-k', required=True, help='Key for encryption/decryption')
    vigenere_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    # ROT13
    rot13_parser = classic_subparsers.add_parser('rot13', help='ROT13 cipher')
    rot13_parser.add_argument('--encode', action='store_true', help='Encode text')
    rot13_parser.add_argument('--decode', action='store_true', help='Decode text')
    rot13_parser.add_argument('--text', '-t', required=True, help='Text to process')
    rot13_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    # Hash command
    hash_parser = subparsers.add_parser('hash', help='Generate hashes')
    hash_parser.add_argument('--file', '-f', help='File to hash')
    hash_parser.add_argument('--text', '-t', help='Text to hash')
    hash_parser.add_argument('--algo', '-a', choices=['md5', 'sha1', 'sha256', 'sha512'], 
                            default='sha256', help='Hash algorithm (default: sha256)')
    hash_parser.add_argument('--compare', '-c', help='Compare hash against this value')
    hash_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    # Check password strength
    checkpw_parser = subparsers.add_parser('checkpw', help='Check password strength')
    checkpw_parser.add_argument('--password', '-p', required=True, help='Password to check')
    checkpw_parser.add_argument('--common', action='store_true',
                               help='Check against common passwords list')
    checkpw_parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == 'encrypt':
            handle_encrypt(args)
        elif args.command == 'decrypt':
            handle_decrypt(args)
        elif args.command == 'classic':
            handle_classic(args)
        elif args.command == 'hash':
            handle_hash(args)
        elif args.command == 'checkpw':
            handle_checkpw(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def handle_encrypt(args):
    if args.file:
        with open(args.file, 'rb') as f:
            data = f.read()
    elif args.text:
        data = args.text.encode('utf-8')
    else:
        raise ValueError("Either --file or --text must be specified")
    
    encrypted = crypto.encrypt(data, args.password)
    
    if args.output:
        with open(args.output, 'wb') as f:
            f.write(encrypted)
    else:
        sys.stdout.buffer.write(encrypted)

def handle_decrypt(args):
    if args.file:
        with open(args.file, 'rb') as f:
            data = f.read()
    elif args.text:
        data = args.text.encode('utf-8')
    else:
        raise ValueError("Either --file or --text must be specified")
    
    decrypted = crypto.decrypt(data, args.password)
    
    if args.output:
        with open(args.output, 'wb') as f:
            f.write(decrypted)
    else:
        sys.stdout.buffer.write(decrypted)

def handle_classic(args):
    if args.cipher == 'caesar':
        if args.encode:
            result = classic.caesar_encode(args.text, args.shift)
        elif args.decode:
            result = classic.caesar_decode(args.text, args.shift)
        else:
            raise ValueError("Either --encode or --decode must be specified")
    elif args.cipher == 'vigenere':
        if args.encode:
            result = classic.vigenere_encode(args.text, args.key)
        elif args.decode:
            result = classic.vigenere_decode(args.text, args.key)
        else:
            raise ValueError("Either --encode or --decode must be specified")
    elif args.cipher == 'rot13':
        if args.encode:
            result = classic.rot13_encode(args.text)
        elif args.decode:
            result = classic.rot13_decode(args.text)
        else:
            raise ValueError("Either --encode or --decode must be specified")
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
    else:
        print(result)

def handle_hash(args):
    if args.file:
        with open(args.file, 'rb') as f:
            data = f.read()
    elif args.text:
        data = args.text.encode('utf-8')
    else:
        raise ValueError("Either --file or --text must be specified")
    
    hash_value = hash_utils.hash_data(data, args.algo)
    
    if args.compare:
        if hash_value == args.compare:
            print("Hash matches!")
            sys.exit(0)
        else:
            print("Hash does not match!")
            sys.exit(1)
    else:
        if args.output:
            with open(args.output, 'w') as f:
                f.write(hash_value)
        else:
            print(hash_value)

def handle_checkpw(args):
    result = password.check_password_strength(args.password, args.common)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(str(result))
    else:
        print(result)

if __name__ == '__main__':
    main()
