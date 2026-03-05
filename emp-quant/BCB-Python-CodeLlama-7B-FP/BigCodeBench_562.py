import os
import ctypes
import sys
import subprocess
def task_func(filepath):
    if not filepath or not isinstance(filepath, str):
        raise TypeError("Invalid filepath")
    if not os.path.exists(filepath):
        raise OSError("File not found")

    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Get system information
    system_name = dll.GetSystemName()
    node_name = dll.GetNodeName()
    release = dll.GetRelease()
    version = dll.GetVersion()
    machine = dll.GetMachine()
    python_version = sys.version
    pip_version = subprocess.check_output(["pip", "--version"]).decode("utf-8")

    # Print system information
    print(f"System: {system_name}")
    print(f"Node Name: {node_name}")
    print(f"Release: {release}")
    print(f"Version: {version}")
    print(f"Machine: {machine}")
    print(f"Python Version: {python_version}")
    print(f"PIP Version: {pip_version}")

    # Return the name of the loaded DLL file
    return filepath
filepath = "C:\\Windows\\System32\\kernel32.dll"