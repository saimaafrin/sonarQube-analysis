import os
import ctypes
import sys
import subprocess
def task_func(filepath):
    """
    Loads a DLL file specified by the given filepath, then retrieves and prints system information
    including system name, node name, release, version, machine, Python version, and PIP version.
    This function demonstrates the use of various system-related libraries in Python.

    The format of the printed message is:
    System: <system-name-here>
    Node Name: <node-name-here>
    Release: <release-here>
    Version: <version-here>
    Machine: <type-of-the-machine-here>
    Python Version: <python-version-here> 
    PIP Version: <pip-version-here>

    Parameters:
    filepath (str): The path of the DLL file to be loaded.

    Returns:
    str: The name of the loaded DLL file.

    Raises:
    OSError: if the input filepath is invalid or empty
    TypeError: if the input filepath is not a string
    
    Requirements:
    - ctypes
    - os
    - sys
    - subprocess

    Examples:
    >>> task_func('libc.so.6') # Doctest will vary based on the system and DLL file.
    'libc.so.6'
    >>> isinstance(task_func('libc.so.6'), str)
    True
    """
    if not filepath:
        raise OSError('Invalid filepath.')
    if not isinstance(filepath, str):
        raise TypeError('Invalid filepath.')

    # Load the DLL file.
    lib = ctypes.CDLL(filepath)

    # Retrieve and print system information.
    print('System:', os.uname().system)
    print('Node Name:', os.uname().node)
    print('Release:', os.uname().release)
    print('Version:', os.uname().version)
    print('Machine:', os.uname().machine)
    print('Python Version:', sys.version)
    print('PIP Version:', subprocess.check_output(['pip', '--version']).decode('utf-8'))

    return filepath