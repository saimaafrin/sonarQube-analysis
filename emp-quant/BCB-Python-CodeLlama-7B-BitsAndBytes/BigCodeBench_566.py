
import inspect
import types

def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name, whether it is a lambda function, its arguments, defaults, and annotations.
    """
    # Get the function's name
    func_name = f.__name__

    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)

    # Get the function's arguments
    args = inspect.getfullargspec(f).args

    # Get the function's default values
    defaults = inspect.getfullargspec(f).defaults

    # Get the function's annotations
    annotations = inspect.getfullargspec(f).annotations

    # Create a dictionary with the function's specifications
    func_specs = {
        'name': func_name,
        'is_lambda': is_lambda,
        'args': args,
        'defaults': defaults,
        'annotations': annotations
    }

    return func_specs