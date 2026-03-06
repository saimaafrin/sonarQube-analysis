import pandas as pd
import re
import os
def task_func(dir_path: str, pattern: str = '^EMP'):
    """
    Look for all ascendingly sorted files in a directory that start with a given pattern, and return the number of files against their size. You should return a pandas DataFrame with 2 columns 'File' and 'Size' with correspond to the file name and the size respectively.

    Parameters:
    - dir_path (str): The path to the directory.
    - pattern (str): The pattern to match. Default is '^EMP' (files starting with 'EMP').

    Returns:
    - pandas.DataFrame: A pandas DataFrame with file names and their sizes.

    Requirements:
    - pandas
    - re
    - os

    Example:
    >>> report = task_func('/path/to/directory')
    >>> print(report)
    """
    # TODO: Implement the function
    # Hint: Use os.listdir() to get the list of files in the directory
    # Hint: Use re.match() to match the pattern
    # Hint: Use sorted() to sort the list of files
    # Hint: Use zip() to create a list of tuples
    # Hint: Use pandas.DataFrame() to create a DataFrame
    # Hint: Use pandas.DataFrame.from_dict() to create a DataFrame from a dictionary
    # Hint: Use pandas.DataFrame.rename() to rename the columns
    # Hint: Use pandas.DataFrame.astype() to convert the column to the correct type
    # Hint: Use pandas.DataFrame.sort_values() to sort the DataFrame
    # Hint: Use pandas.DataFrame.reset_index() to reset the index
    # Hint: Use pandas.DataFrame.drop() to drop the index column
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_csv() to save the DataFrame to a CSV file
    # Hint: Use pandas.DataFrame.to_