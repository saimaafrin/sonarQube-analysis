
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Convert numeric values to floats
    df[columns] = df[columns].apply(pd.to_numeric)

    # Draw line chart of data in specified columns
    fig, ax = plt.subplots()
    ax.plot(df[columns])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Line Chart of Data")

    # Compute cube-root of data
    cube_root = df[columns].apply(np.cbrt)

    return (df, ax, cube_root)