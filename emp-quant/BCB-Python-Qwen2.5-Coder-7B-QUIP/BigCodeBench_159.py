
import struct
import io
import gzip
def task_func(newArray):
    # Convert the NumPy array to bytes using struct
    packed_data = struct.pack('f', *newArray)
    # Create a BytesIO object to hold the data for compression
    buf = io.BytesIO()
    # Compress the packed data using gzip
    gzip_data = gzip.compress(packed_data)
    # Return the compressed data
    return gzip_data