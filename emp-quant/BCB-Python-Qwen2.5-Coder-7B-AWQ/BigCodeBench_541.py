import os
import sys
import importlib
from pkgutil import iter_modules
def task_func(package_name):
    """
    Adds all modules of a specified package to the system path.

    Args:
        package_name (str): The name of the package to add modules from.

    Returns:
        list: A list of module names that were added to the system path.

    Raises:
        ImportError: If the package is not installed or cannot be found.
    """
    # Check if the package is installed
    try:
        importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"Package '{package_name}' is not installed. Please install it using pip: pip install {package_name}")

    # Get the path of the package
    package_path = importlib.util.find_spec(package_name).submodule_search_locations[0]

    # Add the package path to the system path
    sys.path.append(package_path)

    # Find all modules in the package
    modules = [name for _, name, _ in iter_modules([package_path])]

    return modules