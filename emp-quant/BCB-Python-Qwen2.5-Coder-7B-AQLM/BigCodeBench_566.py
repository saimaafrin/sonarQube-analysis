
import inspect
import types

def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name,
    whether it is a lambda function, its arguments, defaults, and annotations.
    
    Parameters:
    f (function): The function to inspect.
    
    Returns:
    dict: A dictionary containing details about the function.
    """
    # Check if the function is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function's name
    name = f.__name__
    
    # Get the function's arguments, defaults, and annotations
    argspec = inspect.getfullargspec(f)
    args = argspec.args
    defaults = argspec.defaults
    annotations = argspec.annotations
    
    # Create a dictionary to store the function's specifications
    func_details = {
        'name': name,
        'is_lambda': is_lambda,
        'args': args,
        'defaults': defaults,
        'annotations': annotations
    }
    
    return func_details

lambda_function = lambda x, y: x * y

print(task_func(example_function))
print(task_func(lambda_function))