import inspect
import types
import json
def task_func(f):
    # Check if the input is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function's name
    name = f.__name__
    
    # Get the function's arguments
    argspec = inspect.getfullargspec(f)
    args = argspec.args
    defaults = argspec.defaults
    annotations = argspec.annotations
    
    # Create a dictionary to store the function's specifications
    func_spec = {
        "name": name,
        "args": args,
        "defaults": defaults,
        "annotations": {k: str(v) for k, v in annotations.items()},
        "is_lambda": is_lambda
    }
    
    # Convert the dictionary to a JSON string
    json_str = json.dumps(func_spec, indent=4)
    
    return json_str