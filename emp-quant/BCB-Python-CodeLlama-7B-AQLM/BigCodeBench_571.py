import inspect
import pandas as pd
def task_func(f_list, file_path):
    """
    Exports the specifications of functions in 'f_list' to a CSV file at 'file_path'.

    The CSV file columns are as follows:
    - 'Function Name': The name of the function.
    - 'Number of Arguments': The number of arguments the function takes.
    - 'Defaults': Default values for the function's arguments, if any.
    - 'Annotations': Type annotations of the function's arguments and return value, if any.
    - 'Is Lambda': Boolean value indicating whether the function is a lambda function.

    Each row in the CSV file corresponds to a function in 'f_list'.

    Parameters:
    f_list (list): A list of function objects to inspect. Each element should be a callable object.
    file_path (str): The path (including filename) where the CSV file will be saved. Should be a writable path.

    Returns:
    None

    Requirements:
    - inspect
    - pandas

    Raises:
    - ValueError: If 'f_list' is not a list of functions, 'f_list' is empty, or 'file_path' is not a valid path.
    - IOError: If there's an error in writing to the specified file path.

    Example:
    >>> def f(x): return 2 * x
    >>> def g(x, y=2): return x * y
    >>> task_func([f, g], './function_info.csv')
    >>> os.remove('./function_info.csv')
    """
    if not isinstance(f_list, list):
        raise ValueError('f_list must be a list of functions.')
    if len(f_list) == 0:
        raise ValueError('f_list must contain at least one function.')
    if not isinstance(file_path, str):
        raise ValueError('file_path must be a string.')
    if not file_path.startswith('./'):
        raise ValueError('file_path must be a writable path.')

    # Create a list of function names
    f_names = []
    for f in f_list:
        f_names.append(f.__name__)

    # Create a list of function specifications
    f_specs = []
    for f in f_list:
        # Get the number of arguments
        num_args = len(inspect.signature(f).parameters)

        # Get the default values
        defaults = []
        for arg in inspect.signature(f).parameters.values():
            if arg.default is not inspect.Parameter.empty:
                defaults.append(arg.default)
            else:
                defaults.append('None')

        # Get the annotations
        annotations = []
        for arg in inspect.signature(f).parameters.values():
            if arg.annotation is not inspect.Parameter.empty:
                annotations.append(str(arg.annotation))
            else:
                annotations.append('None')

        # Get whether the function is a lambda function
        is_lambda = False
        if inspect.isfunction(f):
            is_lambda = False
        elif inspect.isbuiltin(f):
            is_lambda = True
        else:
            raise ValueError('f must be a function or a built-in function.')

        # Add the function specification to the list
        f_specs.append([f.__name__, num_args, defaults, annotations, is_lambda])

    # Create a DataFrame from the function specifications
    df = pd.DataFrame(f_specs, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda'])

    # Export the DataFrame to a CSV file
    try:
        df.to_csv(file_path, index=False)
    except IOError:
        raise IOError('There was an error in writing to the specified file path.')

    return None