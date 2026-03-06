
import collections
import pandas as pd

def task_func(my_tuple, path_csv_files):
    result = {}
    
    for file_path in path_csv_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        for col_name in my_tuple:
            if col_name not in df.columns:
                raise ValueError(f"Column '{col_name}' not found in the CSV file.")
            
            # Count occurrences of each value in the column
            value_counts = df[col_name].value_counts().to_dict()
            
            # Store the result in the main dictionary
            if col_name not in result:
                result[col_name] = value_counts
            else:
                result[col_name].update(value_counts)
    
    return result