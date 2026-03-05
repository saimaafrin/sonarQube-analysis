import struct
import zlib
KEY = '470FC614'
def task_func(hex_string=KEY):
    # Convert hex string to float
    float_number = struct.unpack('!f', bytes.fromhex(hex_string))[0]
    
    # Convert float to binary32 format
    binary32 = struct.pack('!f', float_number)
    
    # Compress the binary32 float number
    compressed_data = zlib.compress(binary32)
    
    return compressed_data