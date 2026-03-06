import inspect
import types
def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name,
    whether it is a lambda function, its arguments, defaults, and annotations. This method
    utilizes the inspect and types modules to introspect function properties.

    Parameters:
    f (function): The function to inspect.

    Returns:
    dict: A dictionary containing details about the function, such as its name, if it's a lambda function,
          arguments, default values, and annotations.

    Requirements:
    - inspect
    - types

    Examples:
    >>> def sample_function(x, y=5): return x + y
    >>> result = task_func(sample_function)
    >>> 'sample_function' == result['function_name'] and len(result['args']) == 2
    True
    >>> lambda_func = lambda x: x * 2
    >>> task_func(lambda_func)['is_lambda']
    True
    """
    # Get the function's name
    function_name = f.__name__

    # Get the function's arguments
    args = inspect.getfullargspec(f).args

    # Get the function's default values
    defaults = inspect.getfullargspec(f).defaults

    # Get the function's annotations
    annotations = inspect.getfullargspec(f).annotations

    # Determine if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)

    # Return the function's specifications
    return {
        'function_name': function_name,
        'is_lambda': is_lambda,
        'args': args,
        'defaults': defaults,
        'annotations': annotations
    }