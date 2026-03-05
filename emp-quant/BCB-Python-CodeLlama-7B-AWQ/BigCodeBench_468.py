import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Convert numeric values to floats
    df[columns] = df[columns].apply(pd.to_numeric)

    # Compute the cube root of the data
    cube_root = df[columns].apply(np.cbrt)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df[columns])
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Cube Root of Data")

    # Return the DataFrame, Axes, and Series
    return df, ax, cube_root
file_path = "data.csv"
columns = ["A", "B", "C"]