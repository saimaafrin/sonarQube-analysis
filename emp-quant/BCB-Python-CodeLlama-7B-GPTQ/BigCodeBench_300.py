import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(df):
    """
    Processes a pandas DataFrame with 'Date' and 'Value' columns.
    The 'Value' column contains lists of numbers.
    Converts 'Date' to datetime, splits 'Value' lists into separate columns,
    calculates Z-scores, and creates a box plot for Z-scores over time.
    """
    # Check if the DataFrame has the required columns
    if 'Date' not in df.columns or 'Value' not in df.columns:
        raise KeyError("The DataFrame must have 'Date' and 'Value' columns.")

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Split 'Value' lists into separate columns
    df = df.explode('Value')

    # Calculate Z-scores
    zscores = zscore(df['Value'])

    # Create a box plot of Z-scores over time
    fig, ax = plt.subplots()
    ax.boxplot(zscores, vert=False)
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')
    ax.set_title('Z-Scores Over Time')

    # Return the DataFrame with Z-scores
    return df
df = pd.DataFrame({
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
    'Value': [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
})