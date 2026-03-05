
from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffled_list = l[:]
    shuffle(shuffled_list)
    
    # Create a longer series by cycling through the shuffled list
    series = pd.Series(shuffled_list * 2)
    
    # Function to move n characters from the start to the end
    def move_chars(s, n):
        return s[n:] + s[:n]
    
    # Apply the function to each element in the series
    modified_series = series.apply(lambda x: move_chars(str(x), n))
    
    return modified_series