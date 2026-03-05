import collections
import pandas as pd
def task_func(my_tuple, path_csv_files):
    """
    Count the occurrences of each value in the specified columns in multiple CSV files.
    The function should output with:
        dict: A dictionary where keys are column names and values are dictionaries
        with unique values in the column as keys and their counts as values.
    """
    # Initialize an empty dictionary to store the results
    result = {}

    # Iterate over the CSV files
    for file in path_csv_files:
        # Read the CSV file
        df = pd.read_csv(file)

        # Iterate over the columns specified in the tuple
        for column in my_tuple:
            # Extract the unique values in the column
            unique_values = df[column].unique()

            # Initialize a dictionary to store the counts
            counts = collections.Counter()

            # Iterate over the unique values and count their occurrences
            for value in unique_values:
                counts[value] = df[column].value_counts(value)

            # Add the counts to the result dictionary
            result[column] = counts

    # Return the result dictionary
    return result
path_csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
my_tuple = ('column1', 'column2')