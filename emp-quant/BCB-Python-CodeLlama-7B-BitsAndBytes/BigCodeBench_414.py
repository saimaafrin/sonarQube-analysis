
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    # Remove the specified column from the DataFrame if it exists
    if column in data.columns:
        data = data.drop(columns=[column])

    # Check if there is numeric data to plot
    if data.select_dtypes(include=[np.number]).shape[1] > 0:
        # Plot the modified DataFrame
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.set_title("Plot of Modified DataFrame")
        return data, ax
    else:
        return data, None