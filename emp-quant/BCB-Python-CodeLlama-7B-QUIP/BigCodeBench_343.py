
import pandas as pd
import matplotlib.pyplot as plt
# Constants for pie chart colors
COLORS = ['r', 'g', 'b', 'y', 'm']
def task_func(df, col, title=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if not df.empty and col in df.columns:
        values = df[col].unique()
        if title:
            plt.title(title)
        fig, ax = plt.subplots()
        ax.pie(values, colors=COLORS)
        return ax
    else:
        raise ValueError("Column {} not found in DataFrame".format(col))