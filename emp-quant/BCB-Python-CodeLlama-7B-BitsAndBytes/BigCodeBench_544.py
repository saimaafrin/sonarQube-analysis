
import struct
import zlib

# Constants
KEY = '470FC614'

def task_func(hex_string=KEY):
    # Convert the hex string to a float number
    float_number = struct.unpack('f', hex_string.decode('hex'))[0]

    # Compress the float number using zlib
    compressed_float_number = zlib.compress(struct.pack('f', float_number))

    # Return the compressed float number
    return compressed_float_number