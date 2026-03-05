import numpy as np
import secrets
import hashlib
import base64
def task_func(num, from_base, to_base, alphabet):
    # Validate the input bases
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be at least 2")
    
    # Validate the number format
    valid_chars = set(alphabet[:from_base])
    if not all(char in valid_chars for char in num):
        raise ValueError("Number contains invalid characters for the specified base")
    
    # Convert the number from the original base to decimal
    decimal_num = int(num, from_base)
    
    # Generate a random salt
    salt = secrets.token_hex(16)
    
    # Convert the decimal number to the target base
    converted_num = ''
    while decimal_num > 0:
        converted_num = alphabet[decimal_num % to_base] + converted_num
        decimal_num //= to_base
    
    # Hash the converted number with the salt
    hash_object = hashlib.sha256((converted_num + salt).encode())
    
    # Encode the hash in base64 using the custom alphabet
    base64_hash = base64.urlsafe_b64encode(hash_object.digest()).rstrip(b'=').decode()
    
    # Convert the base64 hash to the custom alphabet
    custom_base64_hash = ''
    for char in base64_hash:
        custom_base64_hash += alphabet.index(char)
    
    return (custom_base64_hash, salt)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'