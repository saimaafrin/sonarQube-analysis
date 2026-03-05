import collections
import pandas as pd
def task_func(my_tuple, path_csv_files):
    """
    Count the occurrences of each value in the specified columns in multiple CSV files.
    :param my_tuple: A tuple of column names
    :param path_csv_files: A list of paths to CSV files
    :return: A dictionary where keys are column names and values are dictionaries
    with unique values in the column as keys and their counts as values.
    """
    # Create an empty dictionary to store the counts
    counts = collections.defaultdict(dict)

    # Iterate over the CSV files
    for path in path_csv_files:
        # Read the CSV file
        df = pd.read_csv(path)

        # Iterate over the columns in the tuple
        for col in my_tuple:
            # Get the unique values in the column
            unique_values = df[col].unique()

            # Iterate over the unique values
            for value in unique_values:
                # Increment the count for the value
                counts[col][value] = counts[col].get(value, 0) + 1

    # Return the counts
    return counts
my_tuple = ("A", "B")
path_csv_files = ["file1.csv", "file2.csv"]