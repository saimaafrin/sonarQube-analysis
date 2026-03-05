
import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    """
    Adds all modules of a specified package to the system path.
    Returns a list of module names that were added to the system path.
    """
    if not importlib.util.find_spec(package_name):
        raise ImportError(f"Package '{package_name}' not found. Please install it using pip install {package_name}")

    package_path = os.path.dirname(importlib.util.find_spec(package_name).fullname)
    added_modules = []

    for module in iter_modules([package_path]):
        module_name = module.name
        sys.path.append(module_path)
        added_modules.append(module_name)

    return added_modules