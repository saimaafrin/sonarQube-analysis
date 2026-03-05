import inspect
import types
import math
def task_func(f):
    # Get the name of the function
    func_name = f.__name__
    
    # Get the default arguments of the function
    defaults = inspect.getfullargspec(f).defaults
    
    # Count the number of lambda functions in default values
    lambda_count = sum(isinstance(default, types.LambdaType) for default in defaults)
    
    # Calculate the square root of the number of arguments
    num_args = len(inspect.getfullargspec(f).args)
    sqrt_num_args = math.sqrt(num_args)
    
    # Return the result as a dictionary
    return {
        'function_name': func_name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }