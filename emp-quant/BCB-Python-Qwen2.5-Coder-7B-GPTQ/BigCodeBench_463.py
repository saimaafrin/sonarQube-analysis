import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_str, separator=",", bins=20):
    """
    Convert a string of numerical values separated by a specified separator into a pandas numerical series with int64,
    and then draw a histogram of the data.
    
    Parameters:
    - data_str (str): A string of numerical values separated by a specified separator.
    - separator (str): The separator used in the data string. Default is ",".
    - bins (int): The number of bins in the histogram. Default is 20.
    
    Returns:
    - tuple: A tuple containing:
        1. Series: A pandas Series of the data converted into integers.
        2. Axes: The Axes object of the plotted histogram.
    """
    if not data_str:
        raise ValueError("Data string is empty.")
    
    try:
        data_list = [int(value) for value in data_str.split(separator)]
        series = pd.Series(data_list, dtype=np.int64)
    except ValueError:
        raise ValueError("Failed to convert data to integers.")
    
    fig, ax = plt.subplots()
    ax.hist(series, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    plt.show()
    
    return series, ax
data_str = "1,2,3,4,5,6,7,8,9,10"