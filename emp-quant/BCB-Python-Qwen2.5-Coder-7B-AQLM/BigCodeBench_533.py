
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    # Validate the base values
    if from_base < 2 or to_base < 2:
        raise ValueError("Base values must be at least 2.")
    
    # Validate the number format
    if not all(char in alphabet[:from_base] for char in num):
        raise ValueError("Number contains invalid characters for the specified base.")
    
    # Convert the number from the original base to decimal
    decimal_num = int(num, from_base)
    
    # Generate a random salt
    salt = secrets.token_hex(4)
    
    # Convert the decimal number to the target base
    converted_num = ''
    while decimal_num > 0:
        converted_num = alphabet[decimal_num % to_base] + converted_num
        decimal_num //= to_base
    
    # Hash the converted number with the salt
    hash_object = hashlib.sha256((converted_num + salt).encode())
    hash_result = hash_object.hexdigest()
    
    # Encode the hash in base64 using the custom alphabet
    base64_encoded = base64.b64encode(hash_result.encode()).decode()
    
    # Replace standard base64 characters with the custom alphabet
    base64_encoded = base64_encoded.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', alphabet))
    
    return base64_encoded, salt