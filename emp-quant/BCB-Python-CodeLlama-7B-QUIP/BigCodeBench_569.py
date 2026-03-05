
import inspect
import types
import math

def task_func(f):
    # Get the function's name
    func_name = f.__name__

    # Get the number of arguments
    num_args = len(inspect.getfullargspec(f).args)

    # Get the count of lambda functions in default values
    num_lambdas = 0
    for default_value in inspect.getfullargspec(f).defaults:
        if type(default_value) == types.LambdaType:
            num_lambdas += 1

    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)

    # Return a dictionary containing the function's name, the square root of the number of arguments, and the count of lambda functions in default values
    return {
        "name": func_name,
        "sqrt_num_args": sqrt_num_args,
        "num_lambdas": num_lambdas
    }