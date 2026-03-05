
import inspect
import types
import math

def task_func(f):
    # Get the function name
    func_name = f.__name__
    
    # Get the number of arguments
    num_args = f.__code__.co_argcount
    
    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)
    
    # Get the default values of the function
    default_values = inspect.getargspec(f).defaults
    
    # Count the number of lambda functions in the default values
    lambda_count = sum(1 for value in default_values if isinstance(value, types.LambdaType))
    
    # Return the dictionary
    return {
        'function_name': func_name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }