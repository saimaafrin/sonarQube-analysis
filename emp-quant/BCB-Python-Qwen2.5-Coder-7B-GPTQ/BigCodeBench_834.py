import binascii
import io
import gzip
def task_func(compressed_hex):
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Use io.BytesIO to create a file-like object from the bytes
        compressed_file = io.BytesIO(compressed_bytes)
        
        # Use gzip to decompress the file-like object
        with gzip.GzipFile(fileobj=compressed_file, mode='rb') as f:
            decompressed_bytes = f.read()
        
        # Convert the decompressed bytes to a UTF-8 string
        decoded_string = decompressed_bytes.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        # Return an error message if an exception occurs
        return str(e)