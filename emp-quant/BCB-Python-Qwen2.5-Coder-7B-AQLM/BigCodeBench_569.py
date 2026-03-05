
import inspect
import types
import math

def task_func(f):
    # Get the function name
    func_name = f.__name__
    
    # Get the number of arguments
    num_args = len(inspect.signature(f).parameters)
    
    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)
    
    # Count the number of lambda functions in default values
    lambda_count = 0
    for default in inspect.signature(f).parameters.values():
        if isinstance(default, types.LambdaType):
            lambda_count += 1
    
    # Return the result as a dictionary
    return {
        'function_name': func_name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }