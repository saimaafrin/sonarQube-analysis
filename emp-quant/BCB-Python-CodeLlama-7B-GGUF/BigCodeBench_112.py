
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas DataFrame")
    if 'Status' not in df.columns:
        raise ValueError("'df' must contain a 'Status' column")

    status_counts = df['Status'].value_counts()
    status_counts = status_counts.sort_index()

    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
    ax.set_title('Status Distribution')

    return ax