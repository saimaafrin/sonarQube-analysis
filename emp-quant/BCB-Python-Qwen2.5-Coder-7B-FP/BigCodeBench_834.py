import binascii
import io
import gzip
def task_func(compressed_hex):
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Create a BytesIO object with the compressed bytes
        compressed_stream = io.BytesIO(compressed_bytes)
        
        # Use gzip to decompress the stream
        with gzip.GzipFile(fileobj=compressed_stream, mode='rb') as f:
            decompressed_bytes = f.read()
        
        # Convert the decompressed bytes to a UTF-8 string
        decoded_string = decompressed_bytes.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        # Return an error message if an exception occurs
        return f"Error: {str(e)}"