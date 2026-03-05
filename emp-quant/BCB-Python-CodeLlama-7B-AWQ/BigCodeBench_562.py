import os
import ctypes
import sys
import subprocess
def task_func(filepath):
    """
    Loads a DLL file specified by the given filepath, then retrieves and prints system information including system name, node name, release, version, machine, Python version, and PIP version.
    This function demonstrates the use of various system-related libraries in Python.
    The format of the printed message is:
    System: <system-name-here> Node Name: <node-name-here> Release: <release-here> Version: <version-here> Machine: <type-of-the-machine-here> Python Version: <python-version-here> PIP Version: <pip-version-here>
    The function should raise the exception for:
    OSError: if the input filepath is invalid or empty
    TypeError: if the input filepath is not a string
    The function should output with:
        str: The name of the loaded DLL file.
    """
    if not filepath:
        raise TypeError("Input filepath is not a string")
    if not os.path.exists(filepath):
        raise OSError("Input filepath is invalid or empty")

    # Load the DLL file
    dll = ctypes.CDLL(filepath)

    # Get system information
    system_name = os.uname().sysname
    node_name = os.uname().nodename
    release = os.uname().release
    version = os.uname().version
    machine = os.uname().machine
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

    return dll.name
filepath = "C:\\Windows\\System32\\kernel32.dll"