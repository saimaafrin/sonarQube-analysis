
import inspect
import types

def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications.

    Args:
        f (function): The function to be inspected.

    Returns:
        dict: A dictionary containing details about the function, such as its name, if it's a lambda function,
              arguments, default values, and annotations.
    """
    # Check if the input is a function
    if not callable(f):
        raise ValueError("Input must be a callable function.")

    # Initialize the result dictionary
    result = {}

    # Get the function name
    result['name'] = f.__name__

    # Check if the function is a lambda function
    result['is_lambda'] = isinstance(f, types.LambdaType)

    # Get the function signature
    sig = inspect.signature(f)
    
    # Extract parameters from the signature
    params = sig.parameters
    
    # Add arguments to the result dictionary
    result['arguments'] = list(params.keys())
    
    # Add default values to the result dictionary
    result['defaults'] = [params[p].default for p in params if params[p].default != inspect.Parameter.empty]
    
    # Add annotations to the result dictionary
    result['annotations'] = {p: params[p].annotation for p in params if params[p].annotation != inspect.Parameter.empty}

    return result

lambda_function = lambda x, y: x * y

print(task_func(example_function))
print(task_func(lambda_function))