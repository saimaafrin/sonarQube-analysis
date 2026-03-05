
import binascii
import urllib.parse

def task_func(url):
    # Extract the 'q' query parameter from the URL
    query_params = urllib.parse.urlparse(url).query
    q_param = urllib.parse.parse_qs(query_params).get('q')

    if q_param:
        try:
            # Decode the hexadecimal string to UTF-8
            decoded_str = bytes.fromhex(q_param).decode('utf-8', errors='ignore')
            # Check if the decoded string is not empty
            if decoded_str:
                return decoded_str
        except (binascii.Error, UnicodeDecodeError):
            # Return None if the decoding fails
            return None
    return None