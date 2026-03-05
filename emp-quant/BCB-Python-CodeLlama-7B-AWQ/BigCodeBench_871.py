import numpy as np
import itertools
def task_func(data_list, file_name):
    """
    This function takes a list of tuples. The first value of each tuple is a string, the other values are numeric. E.g. ('test', 2, 12.4, -2) It calculates the mean over all tuples of the numerical values for each tuple position excluding the first position, and writes the results into a specified text file. The content in the text file is formated as follows: 'Position 'x': 'mean', where x is the current tuple position and 'mean' denotes the computed mean value. Each Position is written in a new line. It returns a list of the calculated mean values. Missing values and non numeric values at positions other than the first are filled / replaced with np.nan. If an empty list is handed to the function an empty list is returned and an empty file is created. The function utilizes the 'numpy' library for numerical operations and the 'itertools' library to handle the iteration through the data structure.
    """
    # Check if the input list is empty
    if not data_list:
        return []

    # Create an empty list to store the mean values
    mean_values = []

    # Iterate over the tuples in the data list
    for tuple in data_list:
        # Extract the numerical values from the tuple
        numerical_values = tuple[1:]

        # Replace missing or non-numeric values with np.nan
        numerical_values = [np.nan if np.isnan(value) else value for value in numerical_values]

        # Calculate the mean of the numerical values
        mean = np.nanmean(numerical_values)

        # Append the mean value to the list of mean values
        mean_values.append(mean)

    # Write the mean values to a file
    with open(file_name, 'w') as f:
        for i, mean in enumerate(mean_values):
            f.write(f'Position {i}: {mean}\n')

    return mean_values
data_list = [('test', 2, 12.4, -2), ('test2', 3, 12.4, -3), ('test3', 4, 12.4, -4)]
file_name = 'output.txt'