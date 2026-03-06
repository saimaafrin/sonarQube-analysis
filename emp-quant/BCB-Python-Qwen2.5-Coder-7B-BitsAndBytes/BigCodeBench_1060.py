
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame, column_name: str) -> (str, plt.Axes):
    # Check if the DataFrame is empty or the column does not exist
    if df.empty or column_name not in df.columns:
        return "The DataFrame is empty or the specified column has no data.", plt.figure().add_subplot(111)
    
    # Check for null values in the column
    if df[column_name].isnull().all():
        return "The DataFrame is empty or the specified column has no data.", plt.figure().add_subplot(111)
    
    # Calculate the distribution of values
    value_counts = df[column_name].value_counts()
    
    # Determine if the distribution is uniform
    if len(value_counts) == 1:
        uniformity_message = "The distribution of values is uniform."
    else:
        uniformity_message = "The distribution of values is not uniform."
    
    # Create a histogram to visualize the distribution
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts.values, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of values in {column_name}')
    
    return uniformity_message, ax