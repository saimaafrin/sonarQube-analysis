import pandas as pd
import itertools
import random
def task_func(colors, states):
    """
    Generates a pandas DataFrame containing shuffled combinations of provided colors and states.
    The DataFrame is formatted so that each column represents a series of unique combinations,
    with each combination displayed as "Color:State".

    Parameters:
    - colors (list): A list of strings representing color names.
    - states (list): A list of strings representing state descriptions.

    Returns:
    - df (pandas.DataFrame): A DataFrame where each cell contains a string of the format "Color:State".
      The combinations are distributed across columns, with the number of columns being the lesser
      of the lengths of 'colors' and 'states'.

    Requirements:
    - pandas
    - itertools
    - random

    Note:
    - Cartesian product of 'colors' and 'states',
    - The number of columns in the resulting DataFrame is determined by the smaller number of elements
      in either the 'colors' or 'states' list, ensuring an even distribution without excess empty cells.
    - If the number of combinations is not evenly divisible by the number of columns, some columns
      will have fewer entries.

    Example:
    >>> colors = ['Red', 'Blue', 'Green']
    >>> states = ['Solid', 'Liquid']
    >>> color_state_table = task_func(colors, states)
    >>> print(color_state_table)
      Color:State 1 Color:State 2
    0   Blue:Liquid    Red:Liquid
    1    Blue:Solid   Green:Solid
    2     Red:Solid  Green:Liquid
    """
    # Generate a list of all possible combinations of colors and states
    all_combinations = list(itertools.product(colors, states))

    # Shuffle the list of combinations
    random.shuffle(all_combinations)

    # Determine the number of columns to use
    num_columns = min(len(colors), len(states))

    # Create a list of lists, where each list contains a single combination
    combinations_list = [list(combination) for combination in all_combinations]

    # Create a list of lists, where each list contains a single column
    columns_list = [combinations_list[i::num_columns] for i in range(num_columns)]

    # Create a list of lists, where each list contains a single row
    rows_list = [list(itertools.chain(*column)) for column in columns_list]

    # Create a list of lists, where each list contains a single cell
    cells_list = [list(itertools.chain(*row)) for row in rows_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x[0] + ':' + x[1], column)) for column in cells_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ':'), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(':', ': '), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(': ', ':'), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string
    strings_list = [list(map(lambda x: x.replace(' ', ''), column)) for column in strings_list]

    # Create a list of lists, where each list contains a single string