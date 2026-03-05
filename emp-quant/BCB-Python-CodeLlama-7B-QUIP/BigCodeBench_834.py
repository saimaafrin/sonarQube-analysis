
import binascii
import io
import gzip

def task_func(compressed_hex):
    # Decode the hexadecimal string to bytes
    compressed_bytes = binascii.unhexlify(compressed_hex)

    # Create a gzip file object from the bytes
    gzip_file = io.BytesIO(compressed_bytes)

    # Decompress the gzip file
    decompressed_bytes = gzip.decompress(gzip_file)

    # Convert the decompressed bytes to a string
    decoded_string = decompressed_bytes.decode('utf-8')

    return decoded_string