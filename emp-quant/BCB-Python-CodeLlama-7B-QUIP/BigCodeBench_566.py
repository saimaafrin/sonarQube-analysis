
import inspect
import types

def task_func(f):
    """
    Inspects the given function 'f' and returns its specifications.
    """
    # Get the function name
    func_name = f.__name__

    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)

    # Get the function arguments
    args = inspect.getfullargspec(f).args

    # Get the function default values
    defaults = inspect.getfullargspec(f).default

    # Get the function annotations
    annotations = inspect.getfullargspec(f).annotations

    # Create a dictionary with the function details
    func_details = {
        "name": func_name,
        "is_lambda": is_lambda,
        "args": args,
        "defaults": defaults,
        "annotations": annotations
    }

    return func_details