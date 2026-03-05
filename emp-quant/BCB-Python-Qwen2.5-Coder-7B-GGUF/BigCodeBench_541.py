
import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    try:
        # Attempt to import the package to check if it's installed
        importlib.import_module(package_name)
    except ImportError:
        # Raise an ImportError with a message to install the package
        raise ImportError(f"Package '{package_name}' is not installed. Please install it using pip: pip install {package_name}")

    # Get the path of the package
    package_path = importlib.util.find_spec(package_name).submodule_search_locations[0]

    # Add the package path to the system path
    sys.path.append(package_path)

    # List all modules in the package
    modules = [name for _, name, _ in iter_modules([package_path])]

    return modules