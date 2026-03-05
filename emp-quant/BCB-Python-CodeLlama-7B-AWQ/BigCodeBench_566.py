import inspect
import types
def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name, whether it is a lambda function, its arguments, defaults, and annotations.
    This method utilizes the inspect and types modules to introspect function properties.
    The function should output with:
        dict: A dictionary containing details about the function, such as its name, if it's a lambda function,
        arguments, default values, and annotations.
    """
    # Get the function's name
    name = f.__name__

    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)

    # Get the function's arguments
    args = inspect.getargspec(f).args

    # Get the function's default values
    defaults = inspect.getargspec(f).defaults

    # Get the function's annotations
    annotations = inspect.getargspec(f).annotations

    # Create a dictionary with the function's specifications
    specs = {
        'name': name,
        'is_lambda': is_lambda,
        'args': args,
        'defaults': defaults,
        'annotations': annotations
    }

    return specs