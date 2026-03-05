import pandas as pd
from matplotlib import pyplot as plt
def task_func(arr):
    """
    Calculate the sum of each row in a 2D numpy array and plot these sums as a time series.
    
    Parameters:
    arr (numpy.ndarray): A 2D numpy array of numerical values.
    
    Returns:
    matplotlib.axes._axes.Axes: A plot representing the time series of row sums.
    """
    if arr.size == 0:
        # Create an empty plot if the array is empty
        fig, ax = plt.subplots()
        ax.set_title('Time Series of Row Sums')
        return ax
    
    # Calculate the sum of each row
    row_sums = np.sum(arr, axis=1)
    
    # Create a DataFrame with the row sums and dates
    dates = pd.date_range(start='1/1/2020', periods=row_sums.shape[0])
    df = pd.DataFrame({'Date': dates, 'Row Sum': row_sums})
    
    # Plot the row sums as a time series
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Row Sum'], marker='o')
    ax.set_title('Time Series of Row Sums')
    ax.set_xlabel('Date')
    ax.set_ylabel('Row Sum')
    
    return ax