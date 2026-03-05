
import binascii
import base64
import urllib.parse
import codecs

def task_func(hex_string):
    # Convert hexadecimal string to bytes
    bytes_data = binascii.unhexlify(hex_string)
    
    # Convert bytes to UTF-8 string
    utf8_string = bytes_data.decode('utf-8', errors='ignore')
    
    # Encode UTF-8 string to various formats
    hex_encoded = binascii.hexlify(utf8_string).decode('utf-8')
    base64_encoded = base64.b64encode(utf8_string.encode('utf-8')).decode('utf-8')
    utf16_encoded = utf8_string.encode('utf-16').decode('utf-16')
    utf32_encoded = utf8_string.encode('utf-32').decode('utf-32')
    
    try:
        ascii_encoded = utf8_string.encode('ascii').decode('ascii')
    except UnicodeEncodeError:
        ascii_encoded = 'Not representable in ASCII'
    
    url_encoded = urllib.parse.quote(utf8_string)
    
    rot13_encoded = ''.join([chr((ord(c) - 65 + 13) % 26 + 65) if c.isalpha() and c.isupper() else
                              chr((ord(c) - 97 + 13) % 26 + 97) if c.isalpha() and c.islower() else c for c in utf8_string])
    
    # Return the results in a dictionary
    return {
        'hex': hex_encoded,
        'base64': base64_encoded,
        'utf-8': utf8_string,
        'utf-16': utf16_encoded,
        'utf-32': utf32_encoded,
        'ASCII': ascii_encoded,
        'URL': url_encoded,
        'ROT13': rot13_encoded
    }