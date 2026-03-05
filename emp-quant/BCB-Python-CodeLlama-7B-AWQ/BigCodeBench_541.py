import os
import sys
import importlib
from pkgutil import iter_modules
def task_func(package_name):
    """
    Adds all modules of a specified package to the system path.
    This function is useful for dynamically importing modules from a package that might not be on the standard path.
    """
    if not package_name:
        raise ValueError("Package name cannot be empty")

    package_path = importlib.import_module(package_name).__path__
    if not package_path:
        raise ImportError(f"Package {package_name} not found. Please install it using pip install {package_name}")

    modules = []
    for importer, modname, ispkg in iter_modules(package_path):
        if not ispkg:
            module = importlib.import_module(f"{package_name}.{modname}")
            modules.append(modname)
            sys.path.append(os.path.dirname(module.__file__))

    return modules