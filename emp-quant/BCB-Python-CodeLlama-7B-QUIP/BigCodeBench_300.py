
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Split 'Value' lists into separate columns
    for col in df.columns:
        if col != 'Date':
            df[col] = df[col].apply(lambda x: zscore(x))

    # Create a box plot of Z-scores over time
    fig, ax = plt.subplots()
    ax.boxplot(df['Z-Score'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')
    ax.set_title('Z-Scores Over Time')
    fig.tight_layout()

    return df, fig