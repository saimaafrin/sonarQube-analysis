
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if the CSV file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    # Read the CSV file and convert it to a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Clean the data by removing any rows with missing values
    df = df.dropna()

    # Calculate the mean and median of the data
    mean = df.mean()
    median = df.median()

    # Generate a plot of the data
    plt.plot(df)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Data Visualization")
    plt.savefig(plot_path)

    # Return the mean, median, and plot path
    return mean, median, plot_path