import pandas as pd
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame, column_name: str) -> (str, plt.Axes):
    # Check if the DataFrame is empty or the column does not exist
    if df.empty or column_name not in df.columns:
        plt.figure()
        plt.title(f"Distribution of values in {column_name} (No Data)")
        return "The DataFrame is empty or the specified column has no data.", plt.gca()
    
    # Check if the column contains only null values
    if df[column_name].isnull().all():
        plt.figure()
        plt.title(f"Distribution of values in {column_name} (No Data)")
        return "The DataFrame is empty or the specified column has no data.", plt.gca()
    
    # Calculate the distribution of values
    value_counts = df[column_name].value_counts()
    
    # Check if the distribution is uniform
    if len(value_counts) == 1:
        message = "The distribution of values is uniform."
    else:
        message = "The distribution of values is not uniform."
    
    # Plot the histogram
    plt.figure()
    value_counts.plot(kind='bar', edgecolor='black', alpha=0.7)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title(f"Distribution of values in {column_name}")
    
    return message, plt.gca()