
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the DataFrame has the required columns
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns")

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Split 'Value' lists into separate columns
    value_columns = df['Value'].apply(pd.Series)
    df = df.join(value_columns)

    # Calculate Z-scores
    z_scores = df.drop('Date', axis=1).apply(zscore, axis=0)

    # Plot the box plot
    fig, ax = plt.subplots()
    ax.boxplot(z_scores, vert=False)
    ax.set_title('Z-Scores Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')

    # Return the DataFrame with Z-scores and the figure
    return df, fig