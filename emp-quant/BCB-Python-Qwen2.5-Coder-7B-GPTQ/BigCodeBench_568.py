import inspect
import matplotlib.pyplot as plt
import pandas as pd
def task_func(f_list):
    # Check for lambda functions in the input list
    if any(inspect.islambda(f) for f in f_list):
        raise ValueError("Input contains lambda function")
    
    # Create a list to store function names and their argument counts
    func_data = []
    
    # Iterate through each function in the input list
    for func in f_list:
        # Get the number of arguments for the function
        num_args = len(inspect.signature(func).parameters)
        # Append the function name and argument count to the list
        func_data.append((func.__name__, num_args))
    
    # Create a pandas DataFrame from the function data
    df = pd.DataFrame(func_data, columns=['Function Name', 'Number of Arguments'])
    
    # Plot a bar chart using matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(df['Function Name'], df['Number of Arguments'], color='blue')
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Return the DataFrame
    return df