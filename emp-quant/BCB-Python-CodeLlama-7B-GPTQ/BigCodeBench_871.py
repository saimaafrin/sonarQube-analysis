import numpy as np
import itertools
def task_func(data_list, file_name):
    """
    This function takes a list of tuples. The first value of each tuple is a string, the other values are numeric. E.g. ('test', 2, 12.4, -2) It calculates the mean over all tuples of the numerical values for each tuple position excluding the first, and writes the results into a specified text file. The content in the text file is formated as follows: 'Position 'x': 'mean', where x is the current tuple position and 'mean' denotes the computed mean value. Each Position is written in a new line. It returns a list of the calculated mean values. Missing values and non numeric values at positions other than the first are filled / replaced with np.nan. If an empty list is handed to the function an empty list is returned and an empty file is created. The function utilizes the 'numpy' library for numerical operations and the 'itertools' library to handle the iteration through the data structure.
    """
    # Check if the input list is empty
    if not data_list:
        return []

    # Initialize the output list and the file
    output_list = []
    with open(file_name, 'w') as f:
        # Iterate over the tuples in the input list
        for tuple in data_list:
            # Extract the numerical values from the tuple
            numerical_values = tuple[1:]
            # Calculate the mean of the numerical values
            mean = np.nanmean(numerical_values)
            # Write the result to the file
            f.write(f'Position {tuple[0]}: {mean}\n')
            # Add the mean to the output list
            output_list.append(mean)

    return output_list
data_list = [('test1', 2, 12.4, -2), ('test2', 3, 10.5, 1), ('test3', 4, 11.2, 3)]
file_name = 'output.txt'