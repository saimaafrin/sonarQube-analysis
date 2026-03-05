
import collections
import pandas as pd

def task_func(my_tuple, path_csv_files):
    # Create a dictionary to store the counts
    counts = collections.defaultdict(dict)

    # Loop through the CSV files
    for file in path_csv_files:
        # Read the CSV file
        df = pd.read_csv(file)

        # Loop through the columns in the CSV file
        for col in my_tuple:
            # Get the unique values in the column
            unique_vals = df[col].unique()

            # Loop through the unique values
            for val in unique_vals:
                # Increment the count for the value
                counts[col][val] += 1

    # Return the counts
    return counts