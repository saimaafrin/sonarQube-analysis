from random import shuffle, randint
import pandas as pd
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * 3)  # Cycling through the list 3 times
    
    # Modify each element in the series
    modified_series = series.apply(lambda x: move_chars_to_end(x, n_groups))
    
    return modified_series
def move_chars_to_end(s, n):
    # Randomly select n characters from the start of the string and move them to the end
    if n > len(s):
        n = len(s)
    start_chars = s[:n]
    remaining_chars = s[n:]
    return remaining_chars + start_chars
l = ['apple', 'banana', 'cherry', 'date', 'elderberry']
n_groups = 2