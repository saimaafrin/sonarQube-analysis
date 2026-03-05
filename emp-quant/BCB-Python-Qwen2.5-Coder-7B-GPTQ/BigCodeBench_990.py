import binascii
import base64
import urllib.parse
import codecs
def task_func(hex_string):
    # Convert hexadecimal string to bytes
    bytes_data = binascii.unhexlify(hex_string)
    
    # Convert bytes to UTF-8 string
    utf8_string = bytes_data.decode('utf-8', errors='ignore')
    
    # Encode UTF-8 string into different formats
    encoded_dict = {
        'hex': hex_string,
        'base64': base64.b64encode(bytes_data).decode('utf-8'),
        'utf-8': utf8_string,
        'utf-16': utf8_string.encode('utf-16').decode('utf-16'),
        'utf-32': utf8_string.encode('utf-32').decode('utf-32'),
        'ASCII': utf8_string if utf8_string.isascii() else 'Not representable in ASCII',
        'URL': urllib.parse.quote(utf8_string),
        'ROT13': codecs.encode(utf8_string, 'rot_13')
    }
    
    return encoded_dict