
import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    # Check if the package is installed
    try:
        importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"Package {package_name} is not installed. Please run 'pip install {package_name}' to install it.")

    # Get a list of modules in the package
    modules = []
    for importer, modname, ispkg in iter_modules([package_name]):
        modules.append(modname)

    # Add the modules to the system path
    for modname in modules:
        sys.path.append(os.path.join(package_name, modname))

    return modules