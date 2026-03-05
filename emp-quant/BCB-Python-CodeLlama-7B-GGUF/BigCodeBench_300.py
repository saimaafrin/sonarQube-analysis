
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'Date' and 'Value' columns exist
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("DataFrame must have 'Date' and 'Value' columns")

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Split 'Value' lists into separate columns
    df = df.explode('Value')

    # Calculate Z-scores
    df['Z-Score'] = zscore(df['Value'])

    # Create box plot of Z-scores over time
    fig, ax = plt.subplots()
    ax.boxplot(df['Z-Score'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')
    ax.set_title('Z-Scores Over Time')
    plt.show()

    # Return DataFrame with Z-scores
    return df