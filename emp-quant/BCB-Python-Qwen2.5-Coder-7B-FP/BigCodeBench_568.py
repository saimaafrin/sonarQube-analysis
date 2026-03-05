import inspect
import matplotlib.pyplot as plt
import pandas as pd
def task_func(f_list):
    # Check for lambda functions in the input list
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Input contains lambda function")
    
    # Create a list to store function names and their argument counts
    func_data = []
    
    # Iterate through the list of functions
    for func in f_list:
        # Get the signature of the function
        sig = inspect.signature(func)
        # Count the number of parameters
        num_args = len(sig.parameters)
        # Append the function name and argument count to the list
        func_data.append((func.__name__, num_args))
    
    # Create a DataFrame from the function data
    df = pd.DataFrame(func_data, columns=['Function Name', 'Number of Arguments'])
    
    # Plot a bar chart of the number of arguments for each function
    df.plot(kind='bar', x='Function Name', y='Number of Arguments', legend=False)
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Return the DataFrame
    return df