
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas DataFrame")
    if 'Status' not in df.columns:
        raise ValueError("'df' must contain the 'Status' column")

    # Create a pie chart of the status distribution
    status_counts = df['Status'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
    ax.set_title('Status Distribution')
    ax.set_ylabel('Count')
    ax.set_xlabel('Status')
    return ax