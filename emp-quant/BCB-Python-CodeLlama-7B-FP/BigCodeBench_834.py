import binascii
import io
import gzip
def task_func(compressed_hex):
    """
    Uncompress a gzip-compressed hexadecimal string and decrypt the result to UTF-8.
    :param compressed_hex: The compressed hexadecimal string.
    :return: The decoded and decompressed string in UTF-8 format, or an error message.
    """
    try:
        # Decode the hexadecimal string to bytes.
        compressed_bytes = binascii.unhexlify(compressed_hex)

        # Create a gzip decompressor.
        decompressor = gzip.Decompressor()

        # Decompress the bytes.
        decompressed_bytes = decompressor.decompress(compressed_bytes)

        # Convert the decompressed bytes to a string.
        decoded_string = decompressed_bytes.decode("utf-8")

        # Return the decoded string.
        return decoded_string
    except Exception as e:
        # Return an error message if there was an error.
        return f"Error: {e}"