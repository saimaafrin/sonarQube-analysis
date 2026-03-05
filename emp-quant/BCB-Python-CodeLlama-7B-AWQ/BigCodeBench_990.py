import binascii
import base64
import urllib.parse
import codecs
def task_func(hex_string):
    """
    Convert a hexadecimal string to various encodings.

    Args:
        hex_string (str): A hexadecimal string to be converted.

    Returns:
        dict: A dictionary containing the input string encoded in various formats.
    """
    # Decode the hexadecimal string to bytes
    bytes_string = binascii.unhexlify(hex_string)

    # Convert the bytes to a UTF-8 string
    utf8_string = bytes_string.decode("utf-8")

    # Encode the UTF-8 string in various formats
    encodings = {
        "hex": hex_string,
        "base64": base64.b64encode(bytes_string).decode("utf-8"),
        "utf-8": utf8_string,
        "utf-16": utf8_string.encode("utf-16").decode("utf-16"),
        "utf-32": utf8_string.encode("utf-32").decode("utf-32"),
        "ASCII": codecs.encode(utf8_string, "ascii").decode("ascii"),
        "URL": urllib.parse.quote(utf8_string),
        "ROT13": codecs.encode(utf8_string, "rot_13").decode("rot_13"),
    }

    # Return the dictionary of encodings
    return encodings