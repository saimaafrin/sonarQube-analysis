import re

def is_ipv4(target):
    """
    Test if IPv4 address or not.

    Returns: Boolean, True if target is IPv4 address, else False.
    """
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not pattern.match(target):
        return False
    parts = target.split('.')
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True