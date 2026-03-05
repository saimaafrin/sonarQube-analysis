
import pandas as pd
from matplotlib import pyplot as plt

def task_func(arr):
    # Check if the array is empty
    if arr.size == 0:
        # Create an empty plot
        fig, ax = plt.subplots()
        ax.set_title('Time Series of Row Sums')
        return ax

    # Calculate the sum of each row
    row_sums = arr.sum(axis=1)

    # Create a DataFrame with the row sums
    df = pd.DataFrame(row_sums, columns=['Row Sum'])

    # Create a date range starting from January 1, 2020
    dates = pd.date_range(start='2020-01-01', periods=len(df))

    # Add the date range to the DataFrame
    df['Date'] = dates

    # Plot the row sums as a time series
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Row Sum'], marker='o')
    ax.set_title('Time Series of Row Sums')
    ax.set_xlabel('Date')
    ax.set_ylabel('Row Sum')

    return ax