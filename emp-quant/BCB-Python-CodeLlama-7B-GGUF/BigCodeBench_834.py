
import binascii
import io
import gzip

def task_func(compressed_hex):
    # Decode the hexadecimal string to bytes
    compressed_bytes = binascii.unhexlify(compressed_hex)

    # Create a file-like object from the bytes
    compressed_file = io.BytesIO(compressed_bytes)

    # Open the gzip file
    with gzip.open(compressed_file, 'rb') as gz_file:
        # Read the decompressed data
        decompressed_data = gz_file.read()

    # Decode the decompressed data to UTF-8
    decoded_string = decompressed_data.decode('utf-8')

    return decoded_string