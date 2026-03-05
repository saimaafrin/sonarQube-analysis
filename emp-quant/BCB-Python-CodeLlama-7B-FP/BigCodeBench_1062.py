import pandas as pd
import matplotlib.pyplot as plt
def task_func(arr):
    """
    Calculate the sum of each row in a 2D numpy array and plot these sums as a time series.
    This function takes a 2D numpy array and computes the sum of elements in each row.
    It then creates a Pandas DataFrame with these row sums and plots them as a time series,
    using dates starting from January 1, 2020, for each row.
    Handling Scenarios:
    - For non-empty arrays: The function computes the sum of elements for each row,
      stores these sums in a Pandas DataFrame, and then plots them. Each row in the plot
      represents the sum for a specific day, starting from January 1, 2020.
    - For empty arrays: The function creates an empty plot with the title 'Time Series of Row Sums'
      but without data. This is achieved by checking if the array size is zero (empty array)
      and if so, creating a subplot without any data.
    """
    # Check if the array is empty
    if arr.size == 0:
        # Create an empty plot with the title 'Time Series of Row Sums'
        fig, ax = plt.subplots()
        ax.set_title('Time Series of Row Sums')
        return ax

    # Compute the sum of elements for each row
    row_sums = arr.sum(axis=1)

    # Create a Pandas DataFrame with the row sums
    df = pd.DataFrame(row_sums, columns=['Row Sums'])

    # Plot the row sums as a time series
    fig, ax = plt.subplots()
    ax.plot(df['Row Sums'])
    ax.set_title('Time Series of Row Sums')
    ax.set_xlabel('Date')
    ax.set_ylabel('Row Sum')
    return ax
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])