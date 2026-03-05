
import pandas as pd
import seaborn as sns
def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a DataFrame")
    if 'Date' not in df.columns or 'Time' not in df.columns or 'Temperature' not in df.columns:
        raise ValueError("'df' must have 'Date', 'Time', and 'Temperature' columns")
    df = df.set_index('Date')
    df = df.set_index('Time')
    df = df.set_index('Temperature')
    ax = sns.heatmap(df, annot=True)
    return ax