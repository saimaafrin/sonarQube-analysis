
import struct
import zlib

# Constants
KEY = '470FC614'

def task_func(hex_string=KEY):
    # Convert hex string to float
    float_value = struct.unpack('!f', bytes.fromhex(hex_string))[0]
    
    # Compress the float value using zlib
    compressed_data = zlib.compress(struct.pack('!f', float_value))
    
    return compressed_data