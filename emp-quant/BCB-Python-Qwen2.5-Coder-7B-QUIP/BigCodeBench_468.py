
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert numeric values to floats
    df[columns] = df[columns].astype(float)
    
    # Draw a line chart of the data in the specified columns
    fig, ax = plt.subplots()
    ax.plot(df[columns], marker='o')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Line Chart of Data')
    
    # Compute the cube-root of the data
    cube_root = df[columns].applymap(np.cbrt)
    
    # Return the DataFrame, Axes, and Series
    return df, ax, cube_root