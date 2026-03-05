from random import shuffle, randint
import pandas as pd
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * 2)
    
    # Modify each element by moving n characters from the start to the end
    modified_series = series.apply(lambda x: x[n_groups:] + x[:n_groups])
    
    return modified_series
l = ['apple', 'banana', 'cherry', 'date', 'elderberry']
n_groups = 2