
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    # Remove the specified column from the DataFrame
    df = data.drop(columns=column)

    # Check if the DataFrame contains numeric data
    if df.select_dtypes(include=[np.number]).shape[1] > 0:
        # Plot the remaining data
        ax = df.plot(kind="scatter", x="a", y="b")
    else:
        ax = None

    return df, ax