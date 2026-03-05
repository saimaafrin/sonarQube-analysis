
import inspect
import types
import math

def task_func(f):
    """
    Analyzes a given function 'f' and returns a dictionary containing its name, the square root of the number of arguments, and the count of lambda functions present in its default values.
    """
    # Get the function's name and number of arguments
    name = f.__name__
    num_args = len(inspect.signature(f).parameters)

    # Get the count of lambda functions in default values
    default_values = inspect.signature(f).parameters.values()
    lambda_count = sum(1 for v in default_values if isinstance(v.default, types.LambdaType))

    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)

    # Return a dictionary containing the function's name, the square root of the number of arguments, and the count of lambda functions in default values
    return {
        'name': name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }