
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
        num_args = len(inspect.signature(func).parameters)
        defaults = [param.default for param in inspect.signature(func).parameters.values() if param.default is not inspect.Parameter.empty]
        annotations = [param.annotation for param in inspect.signature(func).parameters.values() if param.annotation is not inspect.Parameter.empty]
        annotations.append(inspect.signature(func).return_annotation)
        is_lambda = isinstance(func, lambda)
        
        data.append([func_name, num_args, defaults, annotations, is_lambda])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda'])
    
    # Write the DataFrame to a CSV file
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")
    
    return None