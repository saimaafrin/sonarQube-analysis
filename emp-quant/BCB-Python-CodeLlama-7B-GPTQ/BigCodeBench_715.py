import sys
import subprocess
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'
def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    """
    Switch to a specific version of Python and add a specific path to sys.path.
    Note that: This function changes the global Python version and should be used carefully.
    """
    # Check if the Python version is valid
    if python_version not in sys.version_info:
        raise ValueError(f"Invalid Python version: {python_version}")

    # Check if the path to append is valid
    if not os.path.isdir(path_to_append):
        raise ValueError(f"Invalid path to append: {path_to_append}")

    # Switch to the specified Python version
    subprocess.run(f"python{python_version} -m site --user-site")

    # Add the specified path to sys.path
    sys.path.append(path_to_append)

    # Output the Python version and the path that was added
    print(f"Python version: {python_version}")
    print(f"Path added: {path_to_append}")