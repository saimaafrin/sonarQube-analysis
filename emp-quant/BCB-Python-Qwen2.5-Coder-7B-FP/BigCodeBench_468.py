import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Convert numeric values into floats
    df[columns] = df[columns].astype(float)
    
    # Draw a line chart of data in the specified columns
    fig, ax = plt.subplots()
    for column in columns:
        ax.plot(df[column], label=column)
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Line Chart of Data')
    ax.legend()
    
    # Compute the cube-root of the data
    cube_root_series = df[columns].applymap(np.cbrt)
    
    return df, ax, cube_root_series