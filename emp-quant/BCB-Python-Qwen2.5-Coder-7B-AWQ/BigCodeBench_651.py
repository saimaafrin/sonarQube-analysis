import pandas as pd
import time
import matplotlib.pyplot as plt
def task_func(df, target_value):
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(dtype=float), None
    
    # Filter rows where any cell is equal to the target_value
    filtered_df = df[df.eq(target_value).any(axis=1)]
    
    # Count the occurrences of the target_value per column
    count_series = filtered_df.apply(lambda x: (x == target_value).sum())
    
    # Plot the count of such rows per column
    if not count_series.empty:
        count_series.plot(kind='bar')
        plt.xlabel('Columns')
        plt.ylabel('Count of Target Value')
        plt.title('Count of Target Value per Column')
        plt.show()
    else:
        plt.figure()
        plt.axis('off')
        plt.show()
    
    return count_series, plt.gca()
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 1, 1, 1, 1]
})
target_value = 1