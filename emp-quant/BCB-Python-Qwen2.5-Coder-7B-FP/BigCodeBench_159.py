import struct
import io
import gzip
def task_func(newArray):
    # Create a BytesIO object to hold the packed data
    buffer = io.BytesIO()
    
    # Pack the array elements into bytes
    for element in newArray:
        buffer.write(struct.pack('f', element))  # Assuming the array contains floats
    
    # Get the packed data from the BytesIO object
    packed_data = buffer.getvalue()
    
    # Compress the packed data using gzip
    compressed_data = gzip.compress(packed_data)
    
    # Return the compressed data
    return compressed_data