
import collections
import pandas as pd

def task_func(my_tuple, path_csv_files):
    # Initialize a dictionary to store the counts
    result = collections.defaultdict(lambda: collections.defaultdict(int))
    
    # Iterate over the list of CSV file paths
    for file_path in path_csv_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Iterate over the columns specified in my_tuple
        for col in my_tuple:
            # Check if the column exists in the DataFrame
            if col in df.columns:
                # Iterate over the unique values in the column
                for value in df[col].unique():
                    # Increment the count for the column and value
                    result[col][value] += 1
    
    # Return the result dictionary
    return result