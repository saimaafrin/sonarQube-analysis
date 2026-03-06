
import binascii
import io
import gzip

def task_func(compressed_hex):
    try:
        # Convert the hex string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Create a BytesIO object from the compressed bytes
        compressed_stream = io.BytesIO(compressed_bytes)
        
        # Decompress the data using gzip
        with gzip.GzipFile(fileobj=compressed_stream, mode='rb') as f:
            decompressed_data = f.read()
        
        # Decode the decompressed data to UTF-8
        decoded_string = decompressed_data.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        return str(e)