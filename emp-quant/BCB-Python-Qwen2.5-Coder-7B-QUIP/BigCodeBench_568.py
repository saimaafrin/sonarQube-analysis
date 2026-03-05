
import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    # Check if the input list contains lambda functions
    if any(isinstance(f, lambda) for f in f_list):
        raise ValueError("Input list contains lambda functions")

    # Create a list of tuples with function names and their number of arguments
    func_arg_counts = [(func.__name__, func.__code__.co_argcount) for func in f_list]

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(func_arg_counts, columns=['Function Name', 'Number of Arguments'])

    # Draw a bar chart
    df.plot(x='Function Name', y='Number of Arguments', kind='bar', legend=False)
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Return the DataFrame
    return df