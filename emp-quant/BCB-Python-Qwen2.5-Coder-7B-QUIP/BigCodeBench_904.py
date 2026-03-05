
import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y']):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(d)
    
    # Plot the specified keys
    ax = df[keys].plot(kind='line', marker='o')
    
    # Set plot title and labels
    ax.set_title('Plot of specified keys')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    
    # Return the Matplotlib Axes object
    return ax