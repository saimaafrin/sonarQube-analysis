
import hashlib
import random
import struct
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']
def task_func(hex_keys=KEYS, seed=42):
    random.seed(seed)
    hex_key = random.choice(hex_keys)
    try:
        num = struct.unpack('f', hex_key)[0]
    except ValueError:
        raise ValueError("Invalid hexadecimal string")
    return hashlib.md5(struct.pack('f', num)).hexdigest()