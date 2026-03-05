
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
    num_files = sum(int(item) for item in my_list if item.isdigit())
    
    # Check if there are any files to concatenate
    if num_files == 0:
        raise FileNotFoundError("No files found to concatenate")
    
    # Get the list of CSV files to concatenate
    file_list = glob.glob(os.path.join(file_dir, f'*{file_ext}'))
    
    # Check if there are any CSV files in the directory
    if not file_list:
        raise FileNotFoundError("No CSV files found in the specified directory")
    
    # Concatenate the CSV files into a single DataFrame
    df = pd.concat([pd.read_csv(file) for file in file_list[:num_files]])
    
    return df