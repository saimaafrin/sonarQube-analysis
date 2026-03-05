
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, target_value):
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None

    # Filter rows where any cell is equal to the target_value
    filtered_df = df[df.eq(target_value).any(axis=1)]

    # Count the occurrences of the target value per column
    count_per_column = filtered_df.apply(lambda col: (col == target_value).sum())

    # Plot the count of such rows per column
    if not count_per_column.empty:
        count_per_column.plot(kind='bar')
        plt.xlabel('Columns')
        plt.ylabel('Count of Target Value')
        plt.title('Count of Rows with Target Value per Column')
        plt.show()
    else:
        plt.figure()
        plt.axis('off')
        plt.text(0.5, 0.5, 'No rows with target value', fontsize=12, ha='center', va='center')
        plt.show()

    return count_per_column, plt.gca()