import inspect
import types
import json
def task_func(f):
    """
    Inspects the given function 'f' and returns its specifications as a JSON string.
    This includes the function's name, arguments, default values, annotations in a string format, and a boolean indicating if it's a lambda function.
    """
    # Get the function's name
    name = f.__name__

    # Get the function's arguments
    args = inspect.getargspec(f).args

    # Get the function's default values
    defaults = inspect.getargspec(f).defaults

    # Get the function's annotations
    annotations = inspect.getannotations(f)

    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)

    # Create a dictionary with the function's specifications
    specs = {
        "name": name,
        "args": args,
        "defaults": defaults,
        "annotations": annotations,
        "is_lambda": is_lambda
    }

    # Convert the dictionary to a JSON string
    json_string = json.dumps(specs)

    return json_string