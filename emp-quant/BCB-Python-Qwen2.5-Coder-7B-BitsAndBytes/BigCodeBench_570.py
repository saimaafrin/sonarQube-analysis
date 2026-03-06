
import inspect
import types
import json

def task_func(f):
    # Check if the input is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function name
    func_name = f.__name__
    
    # Get the function signature
    sig = inspect.signature(f)
    
    # Extract parameters and their details
    params = []
    for param_name, param in sig.parameters.items():
        param_info = {
            "name": param_name,
            "kind": param.kind.name,
            "default": param.default if param.default != inspect.Parameter.empty else None,
            "annotation": str(param.annotation) if param.annotation != inspect.Parameter.empty else None
        }
        params.append(param_info)
    
    # Create a dictionary to hold the function's specifications
    func_spec = {
        "function_name": func_name,
        "is_lambda": is_lambda,
        "parameters": params
    }
    
    # Convert the dictionary to a JSON string
    return json.dumps(func_spec, indent=4)

lambda_func = lambda x, y: x + y

print(task_func(example_function))
print(task_func(lambda_func))