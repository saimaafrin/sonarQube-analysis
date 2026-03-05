
import inspect
import pandas as pd

def task_func(f_list, file_path):
    if not isinstance(f_list, list) or len(f_list) == 0:
        raise ValueError("f_list must be a non-empty list of functions")
    if not file_path:
        raise ValueError("file_path must be a valid path")

    # Create a DataFrame with the function specifications
    df = pd.DataFrame(columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda'])
    for func in f_list:
        func_name = func.__name__
        func_args = inspect.getfullargspec(func).args
        func_defaults = inspect.getfullargspec(func).default
        func_annotations = inspect.getfullargspec(func).annotations
        func_is_lambda = inspect.islambda(func)
        df.loc[func_name] = [func_name, len(func_args), func_defaults, func_annotations, func_is_lambda]

    # Write the DataFrame to the file
    try:
        df.to_csv(file_path, index=False)
    except IOError:
        raise IOError("Error writing to file")

    return None