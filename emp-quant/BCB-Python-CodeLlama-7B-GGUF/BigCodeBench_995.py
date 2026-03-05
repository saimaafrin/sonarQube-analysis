
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    """
    Processes a CSV file at the given path by reading its contents, cleaning the data, performing statistical analysis, and generating a plot, which is saved to the specified path.

    Parameters:
    file_path (str): The path to the CSV file to be processed.
    plot_path (str): The path where the plot should be saved.

    Returns:
    tuple: A tuple containing the following elements:
        Mean (float): The average value of the data. Returns NaN if data is empty or non-numeric.
        Median (float): The middle value of the data when sorted. Returns NaN if data is empty or non-numeric.
        Plot Path (str): The path where the plot is saved.

    Raises:
    FileNotFoundError: If the CSV file at 'file_path' does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at {file_path}")

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Clean the data
    df = df.dropna()  # Drop any rows with missing values
    df = df.drop_duplicates()  # Drop any duplicate rows
    df = df.drop(columns=["Unnamed: 0"])  # Drop the first column (index)

    # Perform statistical analysis
    mean = df["Value"].mean()
    median = df["Value"].median()

    # Generate the plot
    plt.plot(df["Index"], df["Value"])
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.savefig(plot_path)

    return mean, median, plot_path