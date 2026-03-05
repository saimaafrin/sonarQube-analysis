import hashlib
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS, seed=42):
    """
    Given a list of hexadecimal string keys, this function selects one at random, converts it into a floating-point number, and then computes its MD5 hash. An optional seed parameter allows for deterministic random choices for testing purposes.
    The function should raise the exception for: ValueError: If contains invalid hexadecimal strings.
    The function should output with:
        str: The MD5 hash of the floating-point number derived from the randomly selected hexadecimal string.
    """
    # Check if the input is a list of hexadecimal strings
    if not all(hex_keys):
        raise ValueError("Invalid hexadecimal string")

    # Select a random key from the list
    if seed:
        random.seed(seed)
    random_key = random.choice(hex_keys)

    # Convert the hexadecimal string to a floating-point number
    float_num = struct.unpack('f', bytes.fromhex(random_key))[0]

    # Compute the MD5 hash of the floating-point number
    md5_hash = hashlib.md5(struct.pack('f', float_num)).hexdigest()

    return md5_hash