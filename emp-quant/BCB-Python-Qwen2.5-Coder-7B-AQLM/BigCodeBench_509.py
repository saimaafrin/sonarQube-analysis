
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    try:
        with open(file_path1, mode='r', newline='', encoding='utf-8') as file1, open(file_path2, mode='r', newline='', encoding='utf-8') as file2:
            reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
            reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)
            
            lines1 = list(reader1)
            lines2 = list(reader2)
            
            if not lines1:
                raise ValueError("The first file is empty.")
            if not lines2:
                raise ValueError("The second file is empty.")
            
            differences = []
            max_length = max(len(lines1), len(lines2))
            
            for i in range(max_length):
                line1 = lines1[i] if i < len(lines1) else []
                line2 = lines2[i] if i < len(lines2) else []
                
                diff = list(ndiff(['\t' + ','.join(line1) + '\n'], ['\t' + ','.join(line2) + '\n']))
                for line in diff:
                    if line.startswith('-'):
                        differences.append({'Line Number': i + 1, 'Status': '-', 'Content': line[2:].strip()})
                    elif line.startswith('+'):
                        differences.append({'Line Number': i + 1, 'Status': '+', 'Content': line[2:].strip()})
                    elif line.startswith(' '):
                        differences.append({'Line Number': i + 1, 'Status': ' ', 'Content': line[2:].strip()})
            
            return pd.DataFrame(differences)
    
    except FileNotFoundError:
        raise FileNotFoundError("One or both of the files could not be found.")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")