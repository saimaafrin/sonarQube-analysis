
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def task_func(dictionary, key, value, n=100, bins=30, seed=0):
    if not isinstance(value, (int, float)):
        raise ValueError("Provided value must be a number")
    dictionary[key] = value
    data = np.random.normal(loc=value, scale=value, size=n)
    hist, edges = np.histogram(data, bins=bins)
    return dictionary, pd.Series(data), plt.hist(edges)