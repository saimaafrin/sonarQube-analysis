
import inspect
import types
import json

def task_func(f):
    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function's name
    name = f.__name__
    
    # Get the function's arguments and default values
    argspec = inspect.getfullargspec(f)
    args = argspec.args
    defaults = argspec.defaults or ()
    default_values = {args[i - len(defaults)]: defaults[i] for i in range(len(defaults))}
    
    # Get the function's annotations
    annotations = f.__annotations__
    
    # Create a dictionary containing the function's specifications
    function_spec = {
        "name": name,
        "args": args,
        "default_values": default_values,
        "annotations": str(annotations),
        "is_lambda": is_lambda
    }
    
    # Convert the dictionary to a JSON string
    json_string = json.dumps(function_spec, indent=4)
    
    return json_string