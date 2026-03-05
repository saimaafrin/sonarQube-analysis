
import struct
import zlib
# Constants
KEY = '470FC614'
def task_func(hex_string=KEY):
    # Convert hex string to float
    float_value = struct.unpack('!f', bytes.fromhex(hex_string))[0]
    
    # Convert float to binary32
    binary32 = struct.pack('!f', float_value)
    
    # Compress the binary32
    compressed = zlib.compress(binary32)
    
    # Output the compressed bytes
    print(f"bytes: {compressed}")