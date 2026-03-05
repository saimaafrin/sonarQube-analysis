import struct
import io
import gzip
def task_func(newArray):
    # Create a BytesIO object to hold the packed data
    output = io.BytesIO()
    
    # Pack the array elements into bytes
    for element in newArray:
        output.write(struct.pack('f', element))  # Assuming the array contains floats
    
    # Get the packed data
    packed_data = output.getvalue()
    
    # Compress the packed data using gzip
    compressed_data = gzip.compress(packed_data)
    
    return compressed_data