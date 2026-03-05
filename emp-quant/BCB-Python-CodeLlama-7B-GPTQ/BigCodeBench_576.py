from random import shuffle, randint
import pandas as pd
def task_func(l, n_groups = 5):
    """
    Generate a Series from a list "l". The function shuffles the list, then creates a longer series by cycling through the shuffled list. For each element in the series, it randomly selects n_groups characters from the start of the string and moves them to the end.
    """
    # Shuffle the list
    shuffle(l)

    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * 2)

    # Randomly select n_groups characters from the start of each string and move them to the end
    for i in range(len(series)):
        start = randint(0, n_groups - 1)
        end = len(series[i]) - start
        series[i] = series[i][start:] + series[i][:start]

    return series
l = ['a', 'b', 'c', 'd', 'e', 'f']
n_groups = 3