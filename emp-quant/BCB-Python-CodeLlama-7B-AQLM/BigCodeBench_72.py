import pandas as pd
import os
import numpy as np
import ast
def task_func(directory):
    """
    Traverse a directory for CSV files a get the file with the longest filename. From that CSV file, load e-mail data, convert it into a Pandas DataFrame, calculate the sum, mean and median of the list associated with each e-mail, and then draw a histogram of the median.
    - The column names of each CSV files are 'email' and 'list'.
    - The column 'list' contains a string representation of a list. It should be converted before usage.
    - If there is not csv file in the directory, return an empty dataframe with the columns expected.
    - If there is not csv file in the directory, return None instead of an empty plot.

    Parameters:
    - directory (str): The path to the directory.

    Returns:
    - pandas.DataFrame : DataFrame containing the data from the CSV file with the longest filename augmented with the columns 'sum', 'mean' and 'median'.
    - matplotlib.axes._axes.Axes : Histogram of the median. None if there is no data to plot.

    Requirements:
    - pandas
    - os
    - numpy
    - ast

    Example:
    >>> task_func('data_directory')
    """
    # TODO: Implement the task
    # Hint: Use the following functions:
    # - os.listdir
    # - os.path.join
    # - os.path.getsize
    # - max
    # - pd.read_csv
    # - pd.DataFrame
    # - pd.Series
    # - pd.concat
    # - pd.DataFrame.sum
    # - pd.DataFrame.mean
    # - pd.DataFrame.median
    # - pd.DataFrame.hist
    # - ast.literal_eval

    # Get the list of files in the directory
    files = os.listdir(directory)

    # Get the longest filename
    longest_filename = max(files, key=len)

    # Get the path to the longest filename
    longest_filename_path = os.path.join(directory, longest_filename)

    # Get the size of the longest filename
    longest_filename_size = os.path.getsize(longest_filename_path)

    # Get the data from the longest filename
    longest_filename_data = pd.read_csv(longest_filename_path)

    # Convert the list column to a list
    longest_filename_data['list'] = longest_filename_data['list'].apply(ast.literal_eval)

    # Get the sum, mean and median of the list associated with each e-mail
    longest_filename_data['sum'] = longest_filename_data['list'].apply(sum)
    longest_filename_data['mean'] = longest_filename_data['list'].apply(np.mean)
    longest_filename_data['median'] = longest_filename_data['list'].apply(np.median)

    # Concatenate the data with the original data
    data = pd.concat([longest_filename_data, longest_filename_data], axis=1)

    # Draw the histogram of the median
    if longest_filename_size > 0:
        data.hist(column='median', bins=100)
        return data
    else:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median'])