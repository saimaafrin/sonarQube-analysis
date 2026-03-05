
import collections
import pandas as pd

def task_func(my_tuple, path_csv_files):
    # Create a dictionary to store the counts for each column
    counts = collections.defaultdict(lambda: collections.defaultdict(int))

    # Loop through each CSV file
    for file_path in path_csv_files:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Loop through each column in the CSV file
        for column in df.columns:
            # Get the unique values in the column
            unique_values = df[column].unique()

            # Loop through each unique value in the column
            for value in unique_values:
                # Increment the count for the value
                counts[column][value] += 1

    # Return the counts dictionary
    return counts