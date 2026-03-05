
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(a, b):
    # Generate random data based on lists 'a' and 'b'
    data = {col: np.random.rand(len(a)) for col in COLUMNS}
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, index=a)
    
    # Plot the DataFrame as a bar chart
    ax = df.plot(kind='bar', stacked=True, figsize=(10, 6))
    
    # Set the plot title and labels
    ax.set_title('Bar Chart of Random Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    
    # Return the Axes object
    return ax