import inspect
import types
import math
def task_func(f):
    # Get the name of the function
    func_name = f.__name__
    
    # Get the number of arguments
    argspec = inspect.getfullargspec(f)
    num_args = len(argspec.args) + len(argspec.kwonlyargs)
    
    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)
    
    # Count the number of lambda functions in default values
    lambda_count = 0
    if argspec.defaults:
        for default in argspec.defaults:
            if isinstance(default, types.LambdaType):
                lambda_count += 1
    
    # Return the result as a dictionary
    return {
        'function_name': func_name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }