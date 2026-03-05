
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_str, separator=",", bins=20):
    if not data_str:
        raise ValueError("Data string is empty")
    
    try:
        data_list = [int(x) for x in data_str.split(separator)]
        series = pd.Series(data_list, dtype=np.int64)
    except ValueError:
        raise ValueError("Failed to convert data to integers")
    
    fig, ax = plt.subplots()
    ax.hist(series, bins=bins, grid=True, rwidth=0.9, color='#607c8e')
    plt.show()
    
    return series, ax