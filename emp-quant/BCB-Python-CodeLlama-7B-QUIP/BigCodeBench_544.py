
import struct
import zlib
# Constants
KEY = '470FC614'
def task_func(hex_string=KEY):
    # Convert hex string to float
    float_value = struct.unpack('f', hex_string)[0]
    # Compress float number
    compressed_float = zlib.compress(float_value)
    return compressed_float