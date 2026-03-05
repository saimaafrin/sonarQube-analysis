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
    random.seed(seed)
    selected_key = random.choice(hex_keys)

    # Convert the selected key to a floating-point number
    selected_key_float = struct.unpack('f', bytes.fromhex(selected_key))[0]

    # Compute the MD5 hash of the floating-point number
    selected_key_md5 = hashlib.md5(struct.pack('f', selected_key_float)).hexdigest()

    return selected_key_md5