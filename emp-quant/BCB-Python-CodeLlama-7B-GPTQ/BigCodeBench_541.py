import os
import sys
import importlib
from pkgutil import iter_modules
def task_func(package_name):
    """
    Adds all modules of a specified package to the system path.
    This function is useful for dynamically importing modules from a package that might not be on the standard path.
    """
    # Check if the package is installed
    try:
        importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"Package '{package_name}' is not installed. Please install it by running 'pip install {package_name}'")

    # Add the package's modules to the system path
    package_path = importlib.import_module(package_name).__path__
    for module_name in iter_modules(package_path):
        module_name = module_name.replace(".", os.sep)
        sys.path.append(os.path.join(package_path, module_name))

    # Return a list of module names that were added to the system path
    return [module_name for module_name in sys.path if module_name.startswith(package_name)]