
import struct
import io
import gzip

def task_func(newArray):
    # Convert the NumPy array to a bytes object
    bytes_array = newArray.tobytes()

    # Use the struct module to pack the array elements into bytes
    packed_bytes = struct.pack('d' * newArray.size, *newArray.flat)

    # Create a BytesIO object to store the compressed data
    compressed_data = io.BytesIO()

    # Compress the packed bytes using gzip
    with gzip.GzipFile(fileobj=compressed_data, mode='wb') as gz:
        gz.write(packed_bytes)

    # Return the compressed data as bytes
    return compressed_data.getvalue()