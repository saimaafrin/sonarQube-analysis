
import pandas as pd
from matplotlib import pyplot as plt

def task_func(arr):
    # Check if the array is empty
    if len(arr) == 0:
        # Create an empty plot with the title 'Time Series of Row Sums'
        fig, ax = plt.subplots(figsize=(10, 6), title='Time Series of Row Sums')
        ax.set_xlabel('Date')
        ax.set_ylabel('Sum of Row Elements')
        ax.set_title('Time Series of Row Sums')
        return ax

    # Compute the sum of elements in each row
    row_sums = arr.sum(axis=1)

    # Create a Pandas DataFrame with the row sums
    df = pd.DataFrame(row_sums, columns=['Sum'])

    # Create a time series plot of the row sums
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Sum'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sum of Row Elements')
    ax.set_title('Time Series of Row Sums')
    return ax