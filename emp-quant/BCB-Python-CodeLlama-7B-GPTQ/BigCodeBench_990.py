import binascii
import base64
import urllib.parse
import codecs
def task_func(hex_string):
    # Decode hexadecimal string to bytes
    bytes_string = binascii.unhexlify(hex_string)

    # Convert bytes to UTF-8 string
    utf8_string = bytes_string.decode('utf-8')

    # Encode UTF-8 string to various formats
    hex_string = codecs.encode(utf8_string, 'hex')
    base64_string = base64.b64encode(utf8_string.encode('utf-8'))
    utf16_string = utf8_string.encode('utf-16')
    utf32_string = utf8_string.encode('utf-32')
    ascii_string = codecs.encode(utf8_string, 'ascii')
    url_string = urllib.parse.quote(utf8_string)
    rot13_string = codecs.encode(utf8_string, 'rot13')

    # Return dictionary with encoded strings
    return {
        'hex': hex_string,
        'base64': base64_string,
        'utf-8': utf8_string,
        'utf-16': utf16_string,
        'utf-32': utf32_string,
        'ASCII': ascii_string,
        'URL': url_string,
        'ROT13': rot13_string
    }