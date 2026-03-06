
from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups=5):
    # Shuffle the list
    shuffle(l)

    # Create a longer series by cycling through the shuffled list
    series = pd.Series(l * 2)

    # Randomly select n_groups characters from the start of the string and move them to the end
    for i in range(n_groups):
        # Select a random index in the series
        idx = randint(0, len(series) - 1)

        # Get the character at the selected index
        char = series[idx]

        # Move the character to the end of the series
        series = series.append(char)

    return series

print(task_func(l, n_groups))