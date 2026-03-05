import struct
import zlib
KEY = '470FC614'
def task_func(hex_string=KEY):
    # Convert hex string to float
    float_number = struct.unpack('!f', bytes.fromhex(hex_string))[0]
    # Compress the float number
    compressed_bytes = zlib.compress(struct.pack('!f', float_number))
    return compressed_bytes