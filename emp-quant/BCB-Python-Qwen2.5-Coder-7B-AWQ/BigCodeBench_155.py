import pandas as pd
import matplotlib.pyplot as plt
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
def task_func(data):
    """
    Computes the average of each row in a provided 2D array and appends these averages as a new column.
    Additionally, it plots the averages against their respective row indices.
    
    Parameters:
    data (list of lists): A 2D array of numerical data.
    
    Returns:
    tuple: A tuple containing:
    - DataFrame: A pandas DataFrame which includes the original data and an additional 'Average' column.
    - Axes: A matplotlib Axes object with the plot of row averages.
    """
    # Convert the 2D array to a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    
    # Calculate the average of each row
    df['Average'] = df.mean(axis=1)
    
    # Plot the averages against their respective row indices
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Average'], marker='o')
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average')
    ax.set_title('Row Averages')
    
    return df, ax
data = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [4, 4, 4, 4, 4, 4, 4, 4]
]