
import binascii
import io
import gzip

def task_func(compressed_hex):
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Create a BytesIO object from the compressed bytes
        compressed_stream = io.BytesIO(compressed_bytes)
        
        # Create a gzip decompression object
        decompression_stream = gzip.GzipFile(fileobj=compressed_stream, mode='rb')
        
        # Read the decompressed data
        decompressed_bytes = decompression_stream.read()
        
        # Decode the bytes to UTF-8
        decoded_string = decompressed_bytes.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        return f"Error: {str(e)}"