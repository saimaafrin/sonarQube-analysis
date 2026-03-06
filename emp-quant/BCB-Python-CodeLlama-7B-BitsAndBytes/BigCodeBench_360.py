
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(file_location, sheet_name):
    # Check if the file exists
    if not os.path.exists(file_location):
        raise FileNotFoundError(f"File {file_location} does not exist")

    # Check if the sheet exists
    if sheet_name not in pd.read_excel(file_location).sheet_names:
        raise ValueError(f"Sheet {sheet_name} does not exist in the workbook")

    # Read the Excel file and calculate the mean and standard deviation of each column
    df = pd.read_excel(file_location, sheet_name=sheet_name)
    means = df.mean(axis=0)
    stds = df.std(axis=0)

    # Create a bar chart of the mean and standard deviation
    fig, ax = plt.subplots()
    ax.bar(range(len(means)), means, yerr=stds)
    ax.set_title("Mean and Standard Deviation")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Values")
    fig.tight_layout()

    # Return the dictionary and figure object
    return {"means": means, "stds": stds, "fig": fig}