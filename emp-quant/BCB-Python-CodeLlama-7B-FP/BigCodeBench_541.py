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

    try:
        package = importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"Package {package_name} is not installed. Please install it using pip.")

    modules = []
    for module in iter_modules(package.__path__):
        module_name = module.name
        module_path = os.path.join(package.__path__, module_name)
        sys.path.append(module_path)
        modules.append(module_name)

    return modules