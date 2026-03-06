
import inspect
import types
import math

def task_func(f):
    # Get the name of the function
    func_name = f.__name__
    
    # Get the signature of the function to determine the number of arguments
    sig = inspect.signature(f)
    num_args = len(sig.parameters)
    
    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)
    
    # Count the number of lambda functions in default values
    lambda_count = 0
    for param in sig.parameters.values():
        if param.default is not inspect.Parameter.empty and isinstance(param.default, types.LambdaType):
            lambda_count += 1
    
    # Create the result dictionary
    result = {
        "function_name": func_name,
        "sqrt_num_args": sqrt_num_args,
        "lambda_count": lambda_count
    }
    
    return result