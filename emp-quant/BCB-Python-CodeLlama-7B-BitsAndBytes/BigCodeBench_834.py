
import binascii
import io
import gzip

def task_func(compressed_hex):
    # Decode the hexadecimal string to bytes
    compressed_bytes = binascii.unhexlify(compressed_hex)

    # Decompress the bytes using gzip
    decompressed_bytes = gzip.decompress(compressed_bytes)

    # Decode the decompressed bytes to a UTF-8 string
    decoded_string = decompressed_bytes.decode("utf-8")

    return decoded_string