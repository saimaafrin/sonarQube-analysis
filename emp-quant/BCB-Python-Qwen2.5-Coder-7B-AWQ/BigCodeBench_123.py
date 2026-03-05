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
    num_files = sum(int(x) for x in my_list if x.isdigit())
    
    # Check if there are files to concatenate
    if num_files == 0:
        raise FileNotFoundError("No files found in the specified directory")
    
    # Get the list of CSV files to concatenate
    file_list = glob.glob(os.path.join(file_dir, f'*{file_ext}'))
    
    # Check if the number of files matches the expected number
    if len(file_list) != num_files:
        raise FileNotFoundError("The number of files in the directory does not match the expected number")
    
    # Concatenate the CSV files into a single DataFrame
    df = pd.concat([pd.read_csv(file) for file in file_list])
    
    return df