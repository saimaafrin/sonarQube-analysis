import pandas as pd
import matplotlib.pyplot as plt
def task_func(arr):
    """
    Calculate the sum of each row in a 2D numpy array and plot these sums as a time series.
    This function takes a 2D numpy array and computes the sum of elements in each row.
    It then creates a Pandas DataFrame with these row sums and plots them as a time series,
    using dates starting from January 1, 2020, for each row.
    Handling Scenarios:
    - For non-empty arrays: The function computes the sum of elements for each row, stores these sums in a Pandas DataFrame, and then plots them.
    Each row in the plot represents the sum for a specific day, starting from January 1, 2020.
    - For empty arrays: The function creates an empty plot with the title 'Time Series of Row Sums' but without data.
    This is achieved by checking if the array size is zero (empty array) and if so, creating a subplot without any data.
    """
    # Check if the array is empty
    if arr.size == 0:
        # Create an empty plot with the title
        fig, ax = plt.subplots(figsize=(10, 6), title='Time Series of Row Sums')
        # Return the plot
        return ax

    # Compute the sum of elements in each row
    row_sums = arr.sum(axis=1)

    # Create a Pandas DataFrame with the row sums
    df = pd.DataFrame(row_sums, columns=['Row Sums'])

    # Convert the dates to a Pandas DatetimeIndex
    df.index = pd.date_range(start='2020-01-01', periods=len(df))

    # Plot the time series
    ax = df.plot(kind='line', figsize=(10, 6), title='Time Series of Row Sums')

    # Return the plot
    return ax
arr = np.array([[1, 2, 3], [4, 5, 6]])