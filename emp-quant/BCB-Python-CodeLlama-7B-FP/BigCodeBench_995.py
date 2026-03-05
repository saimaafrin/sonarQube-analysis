import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def task_func(file_path: str, plot_path: str) -> (float, float, str):
    """
    Processes a CSV file at the given path by reading its contents, cleaning the data, performing statistical analysis, and generating a plot, which is saved to the specified path.
    Sets the title of the plot to "Data Visualization". Labels the x-axis as "Index" and the y-axis as "Value". Saves the generated plot to the file path specified in 'plot_path'.
    The function should raise the exception for: FileNotFoundError: If the CSV file at 'file_path' does not exist.
    The function should output with:
        tuple: A tuple containing the following elements:
        Mean (float): The average value of the data. Returns NaN if data is empty or non-numeric.
        Median (float): The middle value of the data when sorted. Returns NaN if data is empty or non-numeric.
        Plot Path (str): The path where the plot is saved.
    """
    # Check if the CSV file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Clean the data
    df = df.dropna()  # Drop missing values
    df = df.astype(float)  # Convert all values to float

    # Perform statistical analysis
    mean = df.mean()
    median = df.median()

    # Generate the plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df.values)
    ax.set_title("Data Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    plt.savefig(plot_path)

    # Return the results
    return mean, median, plot_path
file_path = "data.csv"
plot_path = "plot.png"