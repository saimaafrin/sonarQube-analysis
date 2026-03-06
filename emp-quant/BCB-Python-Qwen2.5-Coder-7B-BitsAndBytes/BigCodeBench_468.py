
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert numeric values to floats
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].astype(float)
    
    # Select the specified columns
    selected_df = df[columns]
    
    # Draw a line chart of the data
    fig, ax = plt.subplots()
    selected_df.plot(kind='line', ax=ax)
    
    # Compute the cube root of the data
    cube_root_series = np.cbrt(selected_df.values)
    
    return (selected_df, ax, cube_root_series)