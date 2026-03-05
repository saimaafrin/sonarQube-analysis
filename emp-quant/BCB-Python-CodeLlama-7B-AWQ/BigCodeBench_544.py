import struct
import zlib
KEY = '470FC614'
def task_func(hex_string=KEY):
    """
    Converts a given hex string to a float number and then compresses the binary32 float number.
    """
    # Convert hex string to float
    float_number = struct.unpack('f', hex_string.decode('hex'))[0]

    # Compress float number
    compressed_float_number = zlib.compress(struct.pack('f', float_number))

    # Return compressed float number
    return compressed_float_number