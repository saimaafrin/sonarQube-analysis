import struct
import io
import gzip
def task_func(newArray):
    # Pack the array elements into bytes
    packed_data = struct.pack('f' * newArray.size, *newArray.flatten())
    
    # Create a BytesIO object to hold the compressed data
    output = io.BytesIO()
    
    # Compress the packed data using gzip
    with gzip.GzipFile(fileobj=output, mode='wb') as f:
        f.write(packed_data)
    
    # Get the compressed data as bytes
    compressed_data = output.getvalue()
    
    # Close the BytesIO object
    output.close()
    
    return compressed_data