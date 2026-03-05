import re

def is_ipv4(target):
    """
    Test if IPv4 address or not.

    Returns: Boolean, True if target is IPv4 address, else False.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, target):
        parts = target.split('.')
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False