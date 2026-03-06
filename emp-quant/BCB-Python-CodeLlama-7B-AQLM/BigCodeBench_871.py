import numpy as np
import itertools
def task_func(data_list, file_name):
    """
    This function takes a list of tuples. The first value of each tuple is a string,
    the other values are numeric. E.g. ('test', 2, 12.4, -2)
    It calculates the mean over all tuples of the numerical values for each tuple position excluding the first position, 
    and writes the results into a specified text file.
    The content in the text file is formated as follows:
    'Position 'x': 'mean', where x is the current tuple position and 'mean' denotes the 
    computed mean value. Each Position is written in a new line.
    It returns a list of the calculated mean values.

    Missing values and non numeric values at positions other than the first are filled / replaced with np.nan. 
    If an empty list is handed to the function an empty list is returned and an empty file is created.

    The function utilizes the 'numpy' library for numerical operations and the 'itertools' library 
    to handle the iteration through the data structure.

    Parameters:
    - data_list (list of tuples): A list containing tuples of the form (string, numeric, numeric, ...)
    - file_name (str): The name of the text file to store the mean values.

    Returns:
    - list: A list of mean values calculated from the numerical data in the tuples.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> data = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
    >>> task_func(data, 'mean_values.txt')
    [3.0, 4.0]
    >>> with open('mean_values.txt') as file:
    ...    txt_content = file.readlines()
    >>> print(txt_content)
    ['Position 1: 3.0\\n', 'Position 2: 4.0\\n']
    >>> data_list=[('hi', 'test', -12, 4), ('hallo', 1.2, 'test'), ('hola', -3, 34, 12.1)]
    >>> task_func(data_list, 'test.txt')
    [-0.9, 11.0, 8.05]
    >>> with open('test.txt') as file:
    ...     txt_content = file.readlines()
    >>> print(txt_content)
    ['Position 1: -0.9\\n', 'Position 2: 11.0\\n', 'Position 3: 8.05\\n']
    """
    # Check if the data list is empty
    if not data_list:
        # Create an empty file
        with open(file_name, 'w') as file:
            file.write('')
        return []

    # Create a list of the mean values
    mean_list = []

    # Iterate through the data list
    for i in range(1, len(data_list[0])):
        # Create a list of the numeric values
        num_list = []
        # Iterate through the data list
        for data in data_list:
            # Check if the value is a number
            if isinstance(data[i], (int, float)):
                # Add the value to the list
                num_list.append(data[i])
            else:
                # Replace the value with np.nan
                num_list.append(np.nan)
        # Calculate the mean value
        mean_list.append(np.nanmean(num_list))

    # Write the mean values into the text file
    with open(file_name, 'w') as file:
        for i in range(len(mean_list)):
            file.write('Position ' + str(i + 1) + ': ' + str(mean_list[i]) + '\n')

    return mean_list