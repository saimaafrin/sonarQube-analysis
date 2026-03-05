
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    try:
        with open(file_path1, mode='r', newline='', encoding='utf-8') as file1, \
             open(file_path2, mode='r', newline='', encoding='utf-8') as file2:
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
                
                diff = list(ndiff(['\t' + line1], ['\t' + line2]))
                if diff:
                    differences.append({
                        'Line Number': i + 1,
                        'Status': diff[0][0],
                        'Content': diff[0][2:]
                    })
                elif line1 != line2:
                    differences.append({
                        'Line Number': i + 1,
                        'Status': ' ',
                        'Content': '\t' + line1
                    })
            
            return pd.DataFrame(differences)
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"One or both of the files could not be found: {e}")
    except Exception as e:
        raise Exception(f"An IO related error occurred: {e}")