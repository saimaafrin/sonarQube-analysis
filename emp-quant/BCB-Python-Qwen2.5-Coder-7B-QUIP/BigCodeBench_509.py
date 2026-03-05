
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    try:
        with open(file_path1, 'r', newline='', encoding='utf-8') as file1, open(file_path2, 'r', newline='', encoding='utf-8') as file2:
            reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
            reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)

            if not reader1 or not reader2:
                raise ValueError("One or both of the CSV files are empty.")

            diff_df = []
            line_number = 1

            for row1, row2 in zip(reader1, reader2):
                diff = list(ndiff(row1, row2))
                if diff:
                    diff_df.append({
                        'Line Number': line_number,
                        'Status': '-' if diff[0].startswith('-') else '+' if diff[0].startswith('+') else ' ',
                        'Content': diff[0].strip()
                    })

                line_number += 1

            # Check for extra lines in either file
            for row in reader1:
                diff_df.append({
                    'Line Number': line_number,
                    'Status': '-',
                    'Content': row[0] if isinstance(row, list) else row
                })
                line_number += 1

            for row in reader2:
                diff_df.append({
                    'Line Number': line_number,
                    'Status': '+',
                    'Content': row[0] if isinstance(row, list) else row
                })
                line_number += 1

            return pd.DataFrame(diff_df)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}")
    except Exception as e:
        raise Exception(f"IO error: {e}")