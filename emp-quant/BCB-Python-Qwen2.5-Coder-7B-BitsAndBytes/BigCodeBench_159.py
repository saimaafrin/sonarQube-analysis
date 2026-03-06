
import struct
import io
import gzip

def task_func(newArray):
    # Pack the array elements into bytes
    packed_data = newArray.tobytes()
    
    # Create a BytesIO object to hold the compressed data
    compressed_stream = io.BytesIO()
    
    # Compress the packed data using gzip
    with gzip.GzipFile(fileobj=compressed_stream, mode='wb') as f:
        f.write(packed_data)
    
    # Get the compressed data as bytes
    compressed_data = compressed_stream.getvalue()
    
    return compressed_data