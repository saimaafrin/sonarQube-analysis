import subprocess
import platform
import time
def task_func(url):
    """
    Open a web page in the default web browser in a background process.

    Parameters:
    url (str): The URL of the webpage to be opened.

    Returns:
    int: The return code of the subprocess.

    Requirements:
    - subprocess
    - platform
    - time

    Example:
    >>> task_func('https://www.google.com')
    0
    """
    if platform.system() == 'Windows':
        return subprocess.call(['start', url])
    elif platform.system() == 'Darwin':
        return subprocess.call(['open', url])
    elif platform.system() == 'Linux':
        return subprocess.call(['xdg-open', url])
    else:
        return subprocess.call(['xdg-open', url])