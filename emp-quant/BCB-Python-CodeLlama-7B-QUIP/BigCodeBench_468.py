
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path, usecols=columns)

    # Convert the numeric values to floats
    df[columns] = df[columns].apply(lambda x: x.astype(float))

    # Create a line chart of the data
    fig, ax = plt.subplots()
    ax.plot(df["A"], df["B"])
    ax.set_xlabel("A")
    ax.set_ylabel("B")
    ax.set_title("Line Chart of Data")

    # Compute the cube root of the data
    cube_root = df[columns].apply(lambda x: x ** (1/3))

    # Return a tuple containing the DataFrame, axes, and cube root Series
    return (df, ax, cube_root)