import collections
import pandas as pd
def task_func(my_tuple, path_csv_files):
    """
    Count the occurrences of each value in the specified columns in multiple CSV files.

    Args:
        my_tuple: A tuple of column names to count.
        path_csv_files: A list of paths to CSV files.

    Returns:
        A dictionary where keys are column names and values are dictionaries
        with unique values in the column as keys and their counts as values.
    """
    # Create an empty dictionary to store the counts
    counts = {}

    # Loop through each CSV file
    for path in path_csv_files:
        # Read the CSV file
        df = pd.read_csv(path)

        # Loop through each column in the tuple
        for col in my_tuple:
            # Check if the column exists in the DataFrame
            if col in df.columns:
                # Get the unique values in the column
                unique_values = df[col].unique()

                # Create a dictionary to store the counts
                counts[col] = {}

                # Loop through each unique value in the column
                for value in unique_values:
                    # Get the count of the value in the column
                    count = df[col].value_counts()[value]

                    # Add the count to the dictionary
                    counts[col][value] = count

    # Return the counts
    return counts
my_tuple = ("A", "B")
path_csv_files = ["file1.csv", "file2.csv"]