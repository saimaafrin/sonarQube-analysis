
import pandas as pd
import time
def task_func(df, target_value):
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None
    
    # Find rows where any cell is equal to the target value
    matching_rows = df[df.apply(lambda row: row == target_value, axis=1)]
    
    # Count the occurrences of the target value per column
    column_counts = matching_rows.apply(lambda row: row == target_value).sum()
    
    # Plot the count of matching rows per column
    fig, ax = plt.subplots()
    column_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Count of Target Value')
    ax.set_title('Count of Target Value per Column')
    
    return column_counts, ax