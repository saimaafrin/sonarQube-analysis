import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, target_value):
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None
    
    # Filter rows where any cell is equal to the target value
    filtered_df = df[df.eq(target_value).any(axis=1)]
    
    # Count the occurrences of the target value per column
    value_counts = filtered_df.apply(lambda x: (x == target_value).sum())
    
    # Plot the count of such rows per column
    if not value_counts.empty:
        value_counts.plot(kind='bar')
        plt.xlabel('Columns')
        plt.ylabel('Count of Target Value')
        plt.title('Count of Rows with Target Value per Column')
        plt.show()
    else:
        plt.figure()
        plt.axis('off')
        plt.text(0.5, 0.5, 'No rows found with target value', ha='center', va='center')
        plt.show()
    
    return value_counts, plt.gca()
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 1, 1, 1, 1]
})
target_value = 1