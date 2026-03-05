
from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)

    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * n_groups)

    # Randomly select n_groups characters from the start of the string and move them to the end
    for i in range(n_groups):
        # Select a random index in the series
        idx = randint(0, len(series) - 1)

        # Move the selected characters to the end of the string
        series.iloc[idx] = series.iloc[idx][-n_groups:] + series.iloc[idx][:n_groups]

    return series