
import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    # Check for lambda functions in the input list
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Input contains lambda function")
    
    # Create a DataFrame to store function names and their number of arguments
    func_df = pd.DataFrame(columns=['Function Name', 'Number of Arguments'])
    
    # Iterate through the list of functions
    for func in f_list:
        # Get the number of arguments for the function
        num_args = len(inspect.signature(func).parameters)
        # Append the function name and number of arguments to the DataFrame
        func_df = func_df.append({'Function Name': func.__name__, 'Number of Arguments': num_args}, ignore_index=True)
    
    # Plot a bar chart of the number of arguments for each function
    func_df.plot(kind='bar', x='Function Name', y='Number of Arguments', legend=False)
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.show()
    
    # Return the DataFrame
    return func_df