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
    is_uniform = len(value_counts) == 1
    
    # Create a histogram to visualize the distribution
    plt.figure()
    value_counts.plot(kind='bar', edgecolor='black', alpha=0.7)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title(f"Distribution of values in {column_name}")
    
    # Return the message and the Axes object
    return ("The distribution of values is uniform." if is_uniform else "The distribution of values is not uniform."), plt.gca()