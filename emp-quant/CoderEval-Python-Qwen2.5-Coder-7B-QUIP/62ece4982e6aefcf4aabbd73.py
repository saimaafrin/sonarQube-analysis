import os

def split(s, platform='this'):
    if platform == 'this':
        platform = os.name
    elif platform == 1:
        platform = 'posix'
    elif platform == 0:
        platform = 'nt'
    else:
        raise ValueError("Invalid platform")

    if platform == 'posix':
        return s.split()
    elif platform == 'nt':
        return s.split(' ')
    else:
        raise ValueError("Unknown platform")