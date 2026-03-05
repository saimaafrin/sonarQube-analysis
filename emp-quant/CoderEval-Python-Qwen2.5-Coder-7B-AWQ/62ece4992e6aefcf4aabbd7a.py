import os

def is_gitbash():
    return 'MSYS' in os.environ.get('TERM', '') or 'GitBash' in os.environ.get('SHELL', '')