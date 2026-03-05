import os

def is_gitbash():
    """
    Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
    """
    return 'MSYS' in os.environ.get('OS', '')