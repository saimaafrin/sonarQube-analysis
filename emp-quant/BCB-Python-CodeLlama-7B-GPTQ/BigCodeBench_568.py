import inspect
import matplotlib.pyplot as plt
import pandas as pd
def task_func(f_list):
    """
    Analyzes a list of functions and draws a bar chart showing the number of arguments for each function.
    The function names are listed along the x-axis, and the number of arguments are represented as bars.
    This method showcases the integration of function introspection, data frame creation, and data visualization.
    """
    # Check if the input contains lambda function
    if any(inspect.isfunction(f) and f.__name__ == 'lambda' for f in f_list):
        raise ValueError('Lambda function is not allowed in the input list.')

    # Create a DataFrame with function names and their respective number of arguments
    df = pd.DataFrame({'Function': [f.__name__ for f in f_list], 'Arguments': [len(inspect.signature(f).parameters) for f in f_list]})

    # Draw a bar chart with the DataFrame
    df.plot(kind='bar', x='Function', y='Arguments', rot=0)
    plt.show()

    return df
f_list = [lambda x: x**2, lambda y: y**2, lambda z: z**2]