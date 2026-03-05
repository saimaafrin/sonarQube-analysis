
import pandas as pd
import seaborn as sns

def task_func(df, col1, col2):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")
    if not (col1 in df.columns and col2 in df.columns):
        raise ValueError("Columns not found in DataFrame")
    if not (df[col1].dtype == float and df[col2].dtype == float):
        raise TypeError("Columns must be numeric")
    fig, ax = plt.subplots()
    ax.scatter(df[col1], df[col2])
    ax.plot(sm.add_regline(df[col1], df[col2], ax.get_xlim(), ax.get_ylim()))
    return ax