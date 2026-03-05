import inspect
import types
import json
def task_func(f):
    # Check if the input is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function name
    name = f.__name__
    
    # Get the function arguments
    argspec = inspect.getfullargspec(f)
    args = argspec.args
    defaults = argspec.defaults
    annotations = argspec.annotations
    
    # Create a dictionary to store the function specifications
    func_spec = {
        "name": name,
        "is_lambda": is_lambda,
        "args": args,
        "defaults": defaults,
        "annotations": annotations
    }
    
    # Convert the dictionary to a JSON string
    json_str = json.dumps(func_spec, indent=4)
    
    return json_str