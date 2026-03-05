import inspect
import pandas as pd
def task_func(f_list, file_path):
    # Check if f_list is a list of functions
    if not all(callable(f) for f in f_list):
        raise ValueError("f_list must be a list of functions")
    
    # Check if f_list is empty
    if not f_list:
        raise ValueError("f_list cannot be empty")
    
    # Check if file_path is a valid path
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string")
    
    # Create a list to store function specifications
    function_specs = []
    
    # Iterate over each function in f_list
    for func in f_list:
        # Get the function signature
        sig = inspect.signature(func)
        
        # Extract function name
        func_name = func.__name__
        
        # Extract number of arguments
        num_args = len(sig.parameters)
        
        # Extract default values
        defaults = [param.default for param in sig.parameters.values() if param.default is not inspect.Parameter.empty]
        
        # Extract annotations
        annotations = {param: sig.parameters[param].annotation for param in sig.parameters if sig.parameters[param].annotation is not inspect.Parameter.empty}
        annotations['return'] = sig.return_annotation
        
        # Check if the function is a lambda function