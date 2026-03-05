import pandas as pd
import csv
from difflib import ndiff
def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    """
    Compare two CSV files and create a difference report.
    
    Parameters:
    file_path1 (str): The path to the first CSV file.
    file_path2 (str): The path to the second CSV file.
    delimiter (str): The delimiter used in the CSV files. Default is ','.
    quotechar (str): The quote character used in the CSV files. Default is '"'.
    
    Returns:
    pd.DataFrame: A DataFrame with the differences.
    """
    try:
        with open(file_path1, 'r', newline='', encoding='utf-8') as file1, \
             open(file_path2, 'r', newline='', encoding='utf-8') as file2:
            reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
            reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)
            
            # Read all lines from both files
            lines1 = list(reader1)
            lines2 = list(reader2)
            
            # Check if files are empty
            if not lines1:
                raise ValueError("The first file is empty.")
            if not lines2:
                raise ValueError("The second file is empty.")
            
            # Initialize the DataFrame
            differences = []
            
            # Compare lines from both files
            max_length = max(len(lines1), len(lines2))
            for i in range(max_length):
                line1 = lines1[i] if i < len(lines1) else []
                line2 = lines2[i] if i < len(lines2) else []
                
                # Use ndiff to find differences in the lines
                diff = list(ndiff(['\t' + ','.join(line1) + '\n'], ['\t' + ','.join(line2) + '\n']))
                
                # Process the differences
                for d in diff:
                    if d.startswith('-'):
                        differences.append({'Line Number': i + 1, 'Status': '-', 'Content': d[2:]})
                    elif d.startswith('+'):
                        differences.append({'Line Number': i + 1, 'Status': '+', 'Content': d[2:]})
                    elif d.startswith(' '):
                        differences.append({'Line Number': i + 1, 'Status': ' ', 'Content': d[2:]})
            
            # Create the DataFrame
            df = pd.DataFrame(differences)
            return df
    
    except FileNotFoundError:
        raise FileNotFoundError("One or both of the files were not found.")
    except Exception as e:
        raise Exception(f"An IO error occurred: {e}")