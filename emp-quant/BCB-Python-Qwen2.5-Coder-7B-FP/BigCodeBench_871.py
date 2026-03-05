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

    # Initialize a list to store the sum of values for each position
    sums = [0] * num_positions

    # Initialize a list to store the count of non-NaN values for each position
    counts = [0] * num_positions

    # Iterate over each tuple in the data list
    for item in data_list:
        # Iterate over each numeric value in the tuple (excluding the first string)
        for i in range(1, len(item)):
            value = item[i]
            if isinstance(value, (int, float)):
                sums[i-1] += value
                counts[i-1] += 1
            else:
                sums[i-1] += np.nan
                counts[i-1] += 1

    # Calculate the mean for each position
    for i in range(num_positions):
        if counts[i] > 0:
            means.append(sums[i] / counts[i])
        else:
            means.append(np.nan)

    # Write the results to the specified text file
    with open(file_name, 'w') as file:
        for i, mean in enumerate(means, start=1):
            file.write(f'Position {i}: {mean}\n')

    return means