from random import shuffle, randint
import pandas as pd
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * 10)  # Assuming we want a series 10 times longer than the list
    
    # Function to move n characters from the start to the end
    def move_chars(s, n):
        return s[n:] + s[:n]
    
    # Apply the function to each element in the series
    modified_series = series.apply(lambda x: move_chars(x, n_groups))
    
    return modified_series
l = ['apple', 'banana', 'cherry', 'date', 'elderberry']
n_groups = 3