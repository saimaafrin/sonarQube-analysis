
import pandas as pd
import numpy as np

def task_func(data, column="c"):
    # Remove the specified column from the DataFrame
    df = data.drop(columns=[column])

    # Check if the DataFrame contains numeric data
    if df.select_dtypes(np.number).count() > 0:
        # Plot the remaining data
        fig, ax = plt.subplots()
        ax.hist(df.dropna(), bins=50)
        ax.set_xlabel("Value")
        ax.set_ylabel("Count")
        ax.set_title("Histogram of remaining data")
        return df, ax
    else:
        return df, None