
import pandas as pd
import seaborn as sns

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas DataFrame")
    if "Date" not in df.columns or "Time" not in df.columns or "Temperature" not in df.columns:
        raise ValueError("'df' must have 'Date', 'Time', and 'Temperature' columns")

    # Create a Seaborn heatmap with the temperature data
    sns.heatmap(df.pivot_table(index="Date", columns="Time", values="Temperature"))

    # Return the Seaborn heatmap object
    return sns.heatmap