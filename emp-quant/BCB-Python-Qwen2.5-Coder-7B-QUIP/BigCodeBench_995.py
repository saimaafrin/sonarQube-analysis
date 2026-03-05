
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if the CSV file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    # Read the CSV file
    data = pd.read_csv(file_path)

    # Clean the data (assuming the data is in the first column)
    data = data.dropna().astype(float)

    # Calculate mean and median
    mean = data.mean()
    median = data.median()

    # Generate a plot
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o', linestyle='-', color='b')
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.savefig(plot_path)
    plt.close()

    # Return the results
    return (mean, median, plot_path)