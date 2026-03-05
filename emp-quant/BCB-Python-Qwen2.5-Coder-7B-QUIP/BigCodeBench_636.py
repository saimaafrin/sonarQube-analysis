
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(rows):
    # Generate a DataFrame with random integer values between 0 and 9
    data = pd.DataFrame(np.random.randint(0, 10, size=(rows, len(COLUMNS))), columns=COLUMNS)
    
    # Count the non-zero values in each column
    non_zero_counts = data.apply(lambda x: x != 0, axis=0).sum()
    
    # Create a bar plot for the non-zero counts
    fig, ax = plt.subplots()
    non_zero_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Non-zero values')
    ax.set_title('Non-zero values in each column')
    
    return data, ax