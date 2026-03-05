
import struct
import io
import gzip

def compress_array(newArray):
    """
    Compresses a given NumPy array using gzip compression and returns the compressed data.

    Args:
        newArray (numpy.ndarray): The array to be compressed.

    Returns:
        bytes: The gzipped data of the NumPy array.
    """
    # Convert the NumPy array to a bytes object using the struct module
    newArray_bytes = struct.pack('d' * newArray.size, *newArray.flatten())

    # Create a BytesIO object to store the compressed data
    compressed_data = io.BytesIO()

    # Compress the bytes object using gzip
    with gzip.GzipFile(fileobj=compressed_data, mode='wb') as gz:
        gz.write(newArray_bytes)

    # Return the compressed data as bytes
    return compressed_data.getvalue()