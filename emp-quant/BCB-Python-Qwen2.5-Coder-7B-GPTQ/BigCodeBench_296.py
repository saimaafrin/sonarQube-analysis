import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        # Create an empty bar chart
        fig, ax = plt.subplots()
        ax.set_title('Value Distribution')
        ax.set_xlabel('Value')
        ax.set_ylabel('Count')
        return ax
    
    # Count the occurrences of each unique value in the 'value' column
    value_counts = df['value'].value_counts()
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts.values)
    ax.set_title('Value Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Count')
    
    return ax