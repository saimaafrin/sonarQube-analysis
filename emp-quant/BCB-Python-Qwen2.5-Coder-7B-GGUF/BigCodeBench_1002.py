
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column_name="target_column"):
    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Convert non-numeric columns to categorical type and then to numeric codes
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.Categorical(df[col])
            df[col] = df[col].cat.codes
    
    # Plot histogram of the specified column
    ax = df[column_name].hist(bins=10, edgecolor='black')
    ax.set_title(f'Histogram of {column_name}')
    ax.set_xlabel(column_name)
    
    return df, ax