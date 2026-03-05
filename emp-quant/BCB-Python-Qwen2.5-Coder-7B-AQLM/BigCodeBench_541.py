
import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    added_modules = []
    try:
        package = importlib.import_module(package_name)
        package_path = package.__path__
        for _, modname, _ in iter_modules(package_path):
            mod = importlib.import_module(f"{package_name}.{modname}")
            if mod not in sys.modules:
                sys.modules[modname] = mod
                added_modules.append(modname)
    except ImportError:
        raise ImportError(f"Package '{package_name}' not found. Please install it using pip install {package_name}.")
    
    return added_modules