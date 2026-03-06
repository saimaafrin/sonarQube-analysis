
import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    # Check if there is any lambda function in the list
    if any(inspect.islambda(func) for func in f_list):
        raise ValueError("Input contains lambda function")
    
    # Create a dictionary to store function names and their number of arguments
    func_args = {}
    for func in f_list:
        func_args[func.__name__] = len(inspect.signature(func).parameters)
    
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(func_args.items()), columns=['Function Name', 'Number of Arguments'])
    
    # Draw a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Function Name'], df['Number of Arguments'], color='blue')
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments per Function')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return df