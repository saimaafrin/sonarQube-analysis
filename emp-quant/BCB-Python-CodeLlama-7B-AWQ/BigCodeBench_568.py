import inspect
import matplotlib.pyplot as plt
import pandas as pd
def task_func(f_list):
    """
    Analyzes a list of functions and draws a bar chart showing the number of arguments for each function.
    The function names are listed along the x-axis, and the number of arguments are represented as bars.
    This method showcases the integration of function introspection, data frame creation, and data visualization.
    The function should raise the exception for: ValueError: if the input contains lambda function
    The function should output with:
        pandas.DataFrame: Returns a DataFrame containing the function names and their respective number of arguments.
    """
    # Check if the input contains lambda function
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Lambda function is not supported")

    # Create a DataFrame with function names and their respective number of arguments
    df = pd.DataFrame({"Function": [f.__name__ for f in f_list], "Arguments": [len(inspect.signature(f).parameters) for f in f_list]})

    # Draw a bar chart with the DataFrame
    df.plot(kind="bar", x="Function", y="Arguments", rot=0)
    plt.show()

    return df
f_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4]