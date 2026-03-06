
import collections
import pandas as pd

def task_func(my_tuple, path_csv_files):
    # Create a dictionary to store the counts for each column
    counts = collections.defaultdict(dict)

    # Loop through each CSV file in the list
    for file in path_csv_files:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file)

        # Loop through each column in the DataFrame
        for col in df.columns:
            # Get the unique values in the column
            unique_vals = df[col].unique()

            # Loop through each unique value in the column
            for val in unique_vals:
                # Increment the count for the value in the dictionary
                counts[col][val] += 1

    # Return the dictionary of counts
    return counts