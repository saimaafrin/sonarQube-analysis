
import struct
import zlib

# Constants
KEY = '470FC614'

def task_func(hex_string=KEY):
    # Convert hex string to float
    float_number = struct.unpack('f', bytes.fromhex(hex_string))[0]

    # Compress float number using zlib
    compressed_float = zlib.compress(struct.pack('f', float_number))

    # Return compressed float as bytes
    return compressed_float