import os
import ctypes
import sys
import subprocess
def task_func(filepath):
    # Check if the input filepath is valid and is a string
    if not isinstance(filepath, str) or not os.path.exists(filepath):
        raise OSError("Invalid or empty filepath")
    
    # Load the DLL file
    dll = ctypes.CDLL(filepath)
    
    # Retrieve system information
    system_name = os.name
    node_name = os.uname().nodename
    release = os.uname().release
    version = os.uname().version
    machine = os.uname().machine
    python_version = sys.version
    pip_version = subprocess.check_output([sys.executable, '-m', 'pip', '--version']).decode('utf-8').split('\n')[0]
    
    # Print the system information
    print(f"System: {system_name} Node Name: {node_name} Release: {release} Version: {version} Machine: {machine} Python Version: {python_version} PIP Version: {pip_version}")
    
    # Return the name of the loaded DLL file
    return os.path.basename(filepath)