import pandas as pd
import csv
from difflib import ndiff
def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    try:
        with open(file_path1, mode='r', newline='', encoding='utf-8') as file1, \
             open(file_path2, mode='r', newline='', encoding='utf-8') as file2:
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
            
            # Compare lines and create a difference report
            differences = []
            max_length = max(len(lines1), len(lines2))
            for i in range(max_length):
                line1 = lines1[i] if i < len(lines1) else []
                line2 = lines2[i] if i < len(lines2) else []
                diff = list(ndiff(['\t' + ','.join(line1)], ['\t' + ','.join(line2)]))
                for line in diff:
                    if line.startswith('- '):
                        differences.append({'Line Number': i + 1, 'Status': '-', 'Content': line[2:]})
                    elif line.startswith('+ '):
                        differences.append({'Line Number': i + 1, 'Status': '+', 'Content': line[2:]})
                    elif line.startswith('  '):
                        differences.append({'Line Number': i + 1, 'Status': ' ', 'Content': line[2:]})
            
            # Create a DataFrame from the differences
            df = pd.DataFrame(differences)
            return df
    
    except FileNotFoundError:
        raise FileNotFoundError("One or both of the files were not found.")
    except Exception as e:
        raise Exception(f"An IO error occurred: {e}")