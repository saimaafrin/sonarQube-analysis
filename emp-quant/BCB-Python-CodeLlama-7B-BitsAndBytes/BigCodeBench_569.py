
import inspect
import types
import math

def task_func(f):
    # Get the function's name and number of arguments
    name = f.__name__
    num_args = len(inspect.signature(f).parameters)

    # Get the count of lambda functions in default values
    default_values = inspect.signature(f).parameters.values()
    lambda_count = 0
    for default_value in default_values:
        if isinstance(default_value.default, types.LambdaType):
            lambda_count += 1

    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)

    # Return a dictionary containing the function's name, the square root of the number of arguments, and the count of lambda functions in default values
    return {
        'name': name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }

# Print the results
print(task_func(simple_func))
print(task_func(func_with_defaults))
print(task_func(func_with_nested_defaults))