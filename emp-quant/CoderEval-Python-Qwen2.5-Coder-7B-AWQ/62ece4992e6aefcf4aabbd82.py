import re

def get_pattern(pattern, strip=True):
    if isinstance(pattern, str):
        if strip:
            pattern = pattern.strip()
        pattern = re.compile(pattern)
    return pattern