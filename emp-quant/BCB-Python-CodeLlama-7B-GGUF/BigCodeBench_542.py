
import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    """
    Given a list of hexadecimal string keys, this function selects one at random, converts it into a floating-point number, and then computes its MD5 hash.
    An optional seed parameter allows for deterministic random choices for testing purposes.
    """
    if not all(key.isalnum() for key in hex_keys):
        raise ValueError("Invalid hexadecimal string")

    random.seed(seed)
    selected_key = random.choice(hex_keys)

    try:
        float_val = struct.unpack('f', bytes.fromhex(selected_key))[0]
    except struct.error:
        raise ValueError("Invalid hexadecimal string")

    md5_hash = hashlib.md5(struct.pack('f', float_val)).hexdigest()

    return md5_hash