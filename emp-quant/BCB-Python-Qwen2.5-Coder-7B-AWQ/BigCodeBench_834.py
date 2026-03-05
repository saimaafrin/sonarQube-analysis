import binascii
import io
import gzip
def task_func(compressed_hex):
    try:
        # Convert the hexadecimal string to bytes
        compressed_bytes = binascii.unhexlify(compressed_hex)
        
        # Create a BytesIO object from the bytes
        compressed_stream = io.BytesIO(compressed_bytes)
        
        # Create a gzip reader object
        with gzip.GzipFile(fileobj=compressed_stream, mode='rb') as gzip_reader:
            # Read the decompressed data
            decompressed_bytes = gzip_reader.read()
        
        # Convert the decompressed bytes to a UTF-8 string
        decoded_string = decompressed_bytes.decode('utf-8')
        
        return decoded_string
    except Exception as e:
        # Return an error message if an exception occurs
        return str(e)