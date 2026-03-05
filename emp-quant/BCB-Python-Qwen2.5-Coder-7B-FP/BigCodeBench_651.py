import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, target_value):
    """
    Convert the input dictionary of lists to a DataFrame and search for rows with cells equal to the provided target_value.
    It then plots the count of such rows per column.
    
    Parameters:
    df (dict): A dictionary where keys are column names and values are lists of data.
    target_value (any): The value to search for in the DataFrame.
    
    Returns:
    tuple: A tuple containing:
        A pandas Series with counts of the target value per column.
        A matplotlib Axes object representing the plot (None if dataframe is empty).
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(df)
    
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None
    
    # Count the occurrences of the target value per column
    count_series = df.apply(lambda col: (col == target_value).sum())
    
    # Plot the counts
    if not count_series.empty:
        count_series.plot(kind='bar')
        plt.xlabel('Columns')
        plt.ylabel('Count of Target Value')
        plt.title('Count of Target Value per Column')
        plt.show()
    else:
        plt.close()
    
    return count_series, plt.gca() if plt.fignum_exists(1) else None
df = {'A': [1, 2, 3, 4, 5], 'B': [5, 5, 5, 5, 5], 'C': [1, 2, 3, 4, 5]}
target_value = 5