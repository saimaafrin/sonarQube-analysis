
import binascii
import io
import gzip
import base64

def task_func(compressed_hex):
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Decode the base64-encoded bytes
        decoded_bytes = base64.decodes_from_bytes(compressed_bytes)
        
        # Decompress the bytes using gzip
        decompressed_bytes = gzip.decompress(decoded_bytes)
        
        # Convert the decompressed bytes to a UTF-8 string
        decoded_string = decompressed_bytes.decode('utf-8')
        
        return decoded_string
    except (binascii.Error, base64.DecodingError, gzip.GzipError) as e:
        return f"Error: {e}"