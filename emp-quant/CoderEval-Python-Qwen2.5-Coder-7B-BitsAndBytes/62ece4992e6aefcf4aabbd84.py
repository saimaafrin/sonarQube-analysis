import re

def is_ipv4(target):
    """
    Test if IPv4 address or not.

    Returns: Boolean, True if target is IPv4 address, else False.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, target):
        return False
    
    octets = target.split('.')
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False
    
    return True