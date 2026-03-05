
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

def task_func(df, groups=['A', 'B', 'C', 'D', 'E']):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a DataFrame")
    if not set(groups).issubset(df.columns):
        raise ValueError("'df' lacks required columns")

    fig, ax = plt.subplots()
    ax.set_title("Scatterplot of Values for Each Group Over Time")
    ax.set_xlabel("Date (ordinal)")
    ax.set_ylabel("Value")

    colors = cycle(["red", "blue", "green", "yellow", "orange"])
    for group in groups:
        ax.scatter(df[group].index, df[group], c=next(colors))

    return ax