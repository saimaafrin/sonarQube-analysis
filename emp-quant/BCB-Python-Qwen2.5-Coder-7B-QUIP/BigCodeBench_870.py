
import pandas as pd
import numpy as np
import itertools

def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):
    # Initialize a dictionary to store the sums and counts for each position
    sums = {}
    counts = {}

    # Iterate over each tuple in the data list
    for tup in data_list:
        # Iterate over each element in the tuple
        for i, value in enumerate(tup):
            # Check if the value is a number
            if isinstance(value, (int, float)):
                # If the position is not in the dictionary, initialize it with 0
                if i not in sums:
                    sums[i] = 0
                    counts[i] = 0
                # Add the value to the sum and increment the count
                sums[i] += value
                counts[i] += 1

    # Calculate the mean for each position
    means = {i: sums[i] / counts[i] for i in sums}

    # Create a DataFrame with the mean values
    df = pd.DataFrame(list(means.items()), columns=['Position', 'Mean Value'])

    # Set the index to 'Position'
    df.set_index('Position', inplace=True)

    return df