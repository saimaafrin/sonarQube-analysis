
import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    package_path = importlib.import_module(package_name).__path__
    if not os.path.exists(package_path):
        raise ImportError(f"Package {package_name} not found. Please install it using pip install {package_name}.")
    modules = [module for module in iter_modules(package_path) if module.startswith(package_name)]
    sys.path.append(package_path)
    return modules