import inspect
import pandas as pd
def task_func(f_list, file_path):
    if not isinstance(f_list, list) or not f_list:
        raise ValueError("'f_list' must be a non-empty list of functions")
    if not isinstance(file_path, str) or not file_path:
        raise ValueError("'file_path' must be a valid path")

    # Create a list of dictionaries containing function specifications
    specs = []
    for f in f_list:
        spec = {
            "Function Name": f.__name__,
            "Number of Arguments": len(inspect.signature(f).parameters),
            "Defaults": inspect.signature(f).parameters.get("defaults", []),
            "Annotations": inspect.signature(f).annotations,
            "Is Lambda": inspect.isfunction(f)
        }
        specs.append(spec)

    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(specs)

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    return None
f_list = [lambda x: x**2, lambda y: y**2]
file_path = "function_specs.csv"