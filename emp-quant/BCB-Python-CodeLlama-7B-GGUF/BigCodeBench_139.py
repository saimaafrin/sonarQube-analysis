
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    if not df.select_dtypes(include=[np.number]).empty:
        raise ValueError("DataFrame must contain numeric columns")

    # Create a list to store the histogram plots
    plots = []

    # Iterate over the numeric columns in the DataFrame
    for col in df.select_dtypes(include=[np.number]):
        # Create a histogram plot for the current column
        plot = df[col].hist(bins=50, xlabel="Value", ylabel="Frequency", title=col)
        # Add the plot to the list
        plots.append(plot)

    # Return the list of histogram plots
    return plots