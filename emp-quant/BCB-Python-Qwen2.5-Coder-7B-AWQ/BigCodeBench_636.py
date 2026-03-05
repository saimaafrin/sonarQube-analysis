import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
def task_func(rows):
    """
    Generates a DataFrame with random integer values and counts non-zero values in each column.
    
    Parameters:
    rows (int): The number of rows in the DataFrame.
    
    Returns:
    tuple: A tuple containing the DataFrame and the Axes object of the bar plot.
    """
    # Generate a DataFrame with random integer values between 0 and 9
    data = np.random.randint(0, 10, size=(rows, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Count non-zero values in each column
    non_zero_counts = df.count()
    
    # Create a bar plot for the non-zero counts
    fig, ax = plt.subplots()
    ax.bar(non_zero_counts.index, non_zero_counts.values, color='blue')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Non-zero values')
    ax.set_title('Non-zero values count per column')
    
    return df, ax