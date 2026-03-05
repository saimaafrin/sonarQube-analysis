
import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    # Check if the input list contains lambda functions
    if any(map(lambda f: inspect.isfunction(f), f_list)):
        raise ValueError("Lambda functions are not supported")

    # Get the names of the functions in the list
    func_names = [f.__name__ for f in f_list]

    # Get the number of arguments for each function
    func_args = [f.__code__.co_argcount for f in f_list]

    # Create a DataFrame with the function names and their number of arguments
    df = pd.DataFrame({'Function': func_names, 'Arguments': func_args})

    # Create a bar chart with the number of arguments for each function
    fig, ax = plt.subplots()
    ax.bar(df['Function'], df['Arguments'])
    ax.set_xlabel('Function')
    ax.set_ylabel('Number of Arguments')
    ax.set_title('Number of Arguments for Each Function')
    plt.show()

    return df