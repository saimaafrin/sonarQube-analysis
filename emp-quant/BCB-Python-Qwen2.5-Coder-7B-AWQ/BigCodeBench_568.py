import inspect
import matplotlib.pyplot as plt
import pandas as pd
def task_func(f_list):
    # Check for lambda functions in the input list
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Input contains lambda function")
    
    # Create a DataFrame to store function names and their number of arguments
    data = {'Function Name': [], 'Number of Arguments': []}
    
    # Iterate through the list of functions
    for func in f_list:
        # Get the number of arguments for each function
        num_args = len(inspect.signature(func).parameters)
        # Append the function name and number of arguments to the DataFrame
        data['Function Name'].append(func.__name__)
        data['Number of Arguments'].append(num_args)
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Draw a bar chart showing the number of arguments for each function
    plt.bar(df['Function Name'], df['Number of Arguments'])
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.show()
    
    # Return the DataFrame
    return df