import pandas as pd
import os
import glob
def task_func(my_list, file_dir='./data_files/', file_ext='.csv'):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    
    # Add '12' to the list
    my_list.append('12')
    
    # Calculate the number of files to concatenate
    num_files = sum(map(int, my_list))
    
    # Check if there are any files to concatenate
    if num_files == 0:
        raise FileNotFoundError("No files found in the specified directory")
    
    # Construct the file pattern
    file_pattern = os.path.join(file_dir, f'*{file_ext}')
    
    # Get the list of files matching the pattern
    files = glob.glob(file_pattern)
    
    # Check if any files were found
    if not files:
        raise FileNotFoundError("No files found in the specified directory")
    
    # Read the CSV files into a list of DataFrames
    dataframes = [pd.read_csv(file) for file in files[:num_files]]
    
    # Concatenate the DataFrames
    result_df = pd.concat(dataframes, ignore_index=True)
    
    return result_df