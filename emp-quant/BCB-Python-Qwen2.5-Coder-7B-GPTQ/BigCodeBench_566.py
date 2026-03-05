import inspect
import types
def task_func(f):
    # Check if the input is a lambda function
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function name
    name = f.__name__
    
    # Get the function arguments
    argspec = inspect.getfullargspec(f)
    args = argspec.args
    defaults = argspec.defaults
    annotations = argspec.annotations
    
    # Create a dictionary to store the function details
    function_details = {
        'name': name,
        'is_lambda': is_lambda,
        'args': args,
        'defaults': defaults,
        'annotations': annotations
    }
    
    return function_details