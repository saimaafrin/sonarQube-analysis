
import inspect
import types

def task_func(f):
    # Initialize a dictionary to store the function details
    function_details = {}

    # Check if the function is a lambda function
    function_details['is_lambda'] = isinstance(f, types.LambdaType)

    # Get the function name
    function_details['name'] = f.__name__

    # Get the function arguments
    function_details['arguments'] = inspect.getfullargspec(f).args

    # Get the default values for the function arguments
    function_details['defaults'] = inspect.getfullargspec(f).defaults

    # Get the annotations for the function arguments
    function_details['annotations'] = inspect.getfullargspec(f).annotations

    return function_details

# Define a lambda function
lambda_function = lambda x, y: x + y

# Get the function details
print(task_func(sample_function))
print(task_func(lambda_function))