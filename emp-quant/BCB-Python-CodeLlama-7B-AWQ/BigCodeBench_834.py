import binascii
import io
import gzip
def task_func(compressed_hex):
    """
    Uncompress a gzip-compressed hexadecimal string and decrypt the result to UTF-8.
    """
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)

        # Decompress the bytes using gzip
        decompressed_bytes = gzip.decompress(compressed_bytes)

        # Convert the decompressed bytes to a string using UTF-8 encoding
        decoded_string = decompressed_bytes.decode("utf-8")

        return decoded_string
    except Exception as e:
        return "Error: " + str(e)