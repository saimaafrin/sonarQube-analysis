
import inspect
import pandas as pd

def task_func(f_list, file_path):
    # Check if f_list is a list of functions
    if not all(callable(func) for func in f_list):
        raise ValueError("All elements in f_list must be callable functions.")
    
    # Check if f_list is empty
    if not f_list:
        raise ValueError("f_list cannot be empty.")
    
    # Check if file_path is a valid path
    import os
    if not os.path.isfile(file_path):
        raise IOError("Invalid file path.")
    
    # Prepare data for the CSV file
    data = []
    for func in f_list:
        argspec = inspect.getfullargspec(func)
        defaults = argspec.defaults or ()
        annotations = func.__annotations__ if hasattr(func, '__annotations__') else {}
        
        num_args = len(argspec.args)
        default_values = [None] * (num_args - len(defaults)) + list(defaults)
        arg_types = [annotations.get(arg, None) for arg in argspec.args]
        return_type = annotations.get('return', None)
        
        data.append({
            'Function Name': func.__name__,
            'Number of Arguments': num_args,
            'Defaults': default_values,
            'Annotations': {**dict(zip(argspec.args, arg_types)), 'return': return_type},
            'Is Lambda': isinstance(func, type(lambda: 0))
        })
    
    # Create DataFrame and export to CSV
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)