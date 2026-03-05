from random import shuffle, randint
import pandas as pd
def task_func(l, n_groups = 5):
    """
    Generate a Series from a list "l". The function shuffles the list, then creates a longer series by cycling through the shuffled list. For each element in the series, it randomly selects n_groups characters from the start of the string and moves them to the end.
    The function should output with:
        pd.Series: A Series where each element is modified by moving "n"
        characters from the start to the end.
    """
    # Shuffle the list
    shuffle(l)

    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * n_groups)

    # Randomly select n_groups characters from the start of the string and move them to the end
    for i in range(n_groups):
        series = series.str.slice(i, i + n_groups) + series.str.slice(0, i)

    return series
l = ['a', 'b', 'c', 'd', 'e']
n_groups = 3