import numpy as np
import itertools
def task_func(data_list, file_name):
    if not data_list:
        with open(file_name, 'w') as file:
            pass
        return []

    # Initialize a list to store the means
    means = []

    # Extract the number of positions in the tuples (excluding the first string)
    num_positions = len(data_list[0]) - 1

    # Initialize a list to store the sum and count for each position
    sums = [0] * num_positions
    counts = [0] * num_positions

    # Iterate over the data list
    for item in data_list:
        # Check if the item is a tuple and has the correct number of elements
        if isinstance(item, tuple) and len(item) == num_positions + 1:
            for i in range(1, num_positions + 1):
                value = item[i]
                # Check if the value is numeric
                if isinstance(value, (int, float)):
                    sums[i - 1] += value
                    counts[i - 1] += 1
                else:
                    sums[i - 1] += np.nan
                    counts[i - 1] += 1

    # Calculate the mean for each position
    for i in range(num_positions):
        if counts[i] > 0:
            means.append(sums[i] / counts[i])
        else:
            means.append(np.nan)

    # Write the results to the file
    with open(file_name, 'w') as file:
        for i, mean in enumerate(means, start=1):
            file.write(f'Position {i}: {mean}\n')

    return means