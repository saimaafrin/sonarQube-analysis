
import inspect
import types

def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name,
    whether it is a lambda function, its arguments, defaults, and annotations.
    
    :param f: The function to inspect.
    :return: A dictionary containing details about the function.
    """
    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function's name
    name = f.__name__
    
    # Get the function's arguments, defaults, and annotations
    argspec = inspect.getfullargspec(f)
    args = argspec.args
    defaults = argspec.defaults
    annotations = f.__annotations__
    
    # Create a dictionary with the function's details
    function_details = {
        'name': name,
        'is_lambda': is_lambda,
        'args': args,
        'defaults': defaults,
        'annotations': annotations
    }
    
    return function_details

lambda_function = lambda x: x * 2

print(task_func(example_function))
print(task_func(lambda_function))