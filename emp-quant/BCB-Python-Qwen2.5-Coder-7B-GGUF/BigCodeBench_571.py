
import inspect
import pandas as pd

def task_func(f_list, file_path):
    # Check if f_list is a list of functions
    if not isinstance(f_list, list) or not all(callable(f) for f in f_list):
        raise ValueError("f_list must be a list of functions")
    
    # Check if f_list is empty
    if not f_list:
        raise ValueError("f_list cannot be empty")
    
    # Check if file_path is a valid path
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string")
    
    # Prepare data for the CSV file
    data = []
    for func in f_list:
        func_name = func.__name__
        argspec = inspect.getfullargspec(func)
        num_args = len(argspec.args) - len(argspec.defaults) if argspec.defaults else len(argspec.args)
        defaults = argspec.defaults if argspec.defaults else []
        annotations = func.__annotations__ if hasattr(func, '__annotations__') else {}
        is_lambda = inspect.islambda(func)
        
        data.append({
            'Function Name': func_name,
            'Number of Arguments': num_args,
            'Defaults': defaults,
            'Annotations': annotations,
            'Is Lambda': is_lambda
        })
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Write the DataFrame to a CSV file
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")
    
    return None