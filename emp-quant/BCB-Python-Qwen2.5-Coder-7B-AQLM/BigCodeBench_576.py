
from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * 10)  # Repeat the list 10 times to create a longer series
    
    # Modify each element in the series
    modified_series = series.apply(lambda x: x[n_groups:] + x[:n_groups])
    
    return modified_series