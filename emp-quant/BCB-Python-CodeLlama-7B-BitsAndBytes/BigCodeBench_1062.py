
import pandas as pd
from matplotlib import pyplot as plt

def task_func(arr):
    # Check if the array is empty
    if arr.size == 0:
        # Create an empty plot with the title 'Time Series of Row Sums'
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title('Time Series of Row Sums')
        ax.set_xlabel('Date')
        ax.set_ylabel('Sum of Row Elements')
        ax.set_xticks([])
        ax.set_yticks([])
        return ax

    # Compute the sum of elements for each row
    row_sums = arr.sum(axis=1)

    # Create a Pandas DataFrame with the row sums
    df = pd.DataFrame(row_sums, columns=['Sum'])

    # Create a plot with the time series of row sums
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Sum'])
    ax.set_title('Time Series of Row Sums')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sum of Row Elements')
    ax.set_xticks(range(len(df['Sum'])))
    ax.set_xticklabels(df['Sum'].index)
    return ax