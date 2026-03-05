import os

def split(s, platform='this'):
    if platform == 'this':
        platform = os.name
    
    if platform == 'posix':
        return s.split('/')
    elif platform == 'nt':
        return s.split('\\')
    else:
        raise ValueError("Invalid platform specified")