
import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    # Check if any of the functions in the list are lambda functions
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Lambda functions are not supported")

    # Create a dictionary to store the function names and their argument counts
    func_args = {}
    for f in f_list:
        func_args[f.__name__] = len(inspect.signature(f).parameters)

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(func_args, index=["Arguments"])

    # Draw a bar chart of the function names and their argument counts
    df.plot(kind="bar", figsize=(10, 6), rot=0)
    plt.title("Function Argument Counts")
    plt.xlabel("Function Name")
    plt.ylabel("Number of Arguments")
    plt.show()

    return df