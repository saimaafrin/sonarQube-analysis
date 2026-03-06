
import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    try:
        # Attempt to import the package to check if it's already installed
        __import__(package_name)
    except ImportError:
        # Raise an ImportError with instructions to install the package
        raise ImportError(f"Package '{package_name}' is not installed. Please run 'pip install {package_name}'.")

    # Get the directory containing the package
    package_dir = importlib.util.find_spec(package_name).submodule_search_locations[0]

    # List to store the module names that will be added to the system path
    added_modules = []

    # Iterate through the modules in the package directory
    for _, name, _ in iter_modules([package_dir]):
        # Construct the full module name
        full_module_name = f"{package_name}.{name}"
        
        # Add the module to the system path
        sys.path.append(os.path.join(package_dir, name))
        
        # Append the module name to the list
        added_modules.append(full_module_name)

    return added_modules