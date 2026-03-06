
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, target_value):
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(df)
    
    # Check if the DataFrame is empty
    if df.empty:
        return pd.Series(), None
    
    # Create a boolean mask for rows where any cell equals the target_value
    mask = df.apply(lambda row: row.astype(str).str.contains(target_value, na=False)).any(axis=1)
    
    # Filter the DataFrame based on the mask
    filtered_df = df[mask]
    
    # Count the occurrences of the target value per column
    target_counts = filtered_df.apply(lambda col: (col == target_value).sum())
    
    # Plot the count of target values per column
    fig, ax = plt.subplots()
    target_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Count of Target Value')
    ax.set_title('Count of Target Value per Column')
    
    return target_counts, ax

    result_series, plot_ax = task_func(data, target_value)
    print(result_series)
    if plot_ax is not None:
        plt.show()