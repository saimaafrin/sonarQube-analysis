
import pandas as pd
from matplotlib import pyplot as plt

def task_func(arr):
    """
    Calculate the sum of each row in a 2D numpy array and plot these sums as a time series.
    
    Parameters:
    arr (numpy.ndarray): A 2D numpy array.
    
    Returns:
    matplotlib.axes._axes.Axes: A plot representing the time series of row sums.
    """
    if arr.size == 0:
        fig, ax = plt.subplots()
        ax.set_title('Time Series of Row Sums')
        return ax
    
    row_sums = np.sum(arr, axis=1)
    dates = pd.date_range(start='2020-01-01', periods=row_sums.shape[0])
    df = pd.DataFrame(row_sums, index=dates, columns=['Row Sum'])
    
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Row Sum'], marker='o')
    ax.set_title('Time Series of Row Sums')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sum of Row')
    
    return ax