
import inspect
import types
import json

def task_func(f):
    # Get the function's name
    name = f.__name__

    # Get the function's arguments
    args = inspect.signature(f).parameters

    # Get the function's default values
    defaults = inspect.signature(f).parameters.values()

    # Get the function's annotations
    annotations = inspect.getfullargspec(f).annotations

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