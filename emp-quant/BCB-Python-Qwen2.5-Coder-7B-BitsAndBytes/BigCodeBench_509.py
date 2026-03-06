
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    try:
        # Read the CSV files
        df1 = pd.read_csv(file_path1, delimiter=delimiter, quotechar=quotechar)
        df2 = pd.read_csv(file_path2, delimiter=delimiter, quotechar=quotechar)

        # Check if the files are empty
        if df1.empty or df2.empty:
            raise ValueError("One or both of the files are empty.")

        # Initialize an empty list to store differences
        differences = []

        # Compare the two DataFrames line by line
        max_length = max(len(df1), len(df2))
        for i in range(max_length):
            row1 = df1.iloc[i] if i < len(df1) else None
            row2 = df2.iloc[i] if i < len(df2) else None

            if row1 is None:
                differences.append({'Line Number': i + 1, 'Status': '-', 'Content': str(row2)})
            elif row2 is None:
                differences.append({'Line Number': i + 1, 'Status': '+', 'Content': str(row1)})
            else:
                diff = list(ndiff(str(row1).splitlines(), str(row2).splitlines()))
                if any(d.startswith('+') or d.startswith('-') for d in diff):
                    differences.extend({
                        'Line Number': i + 1,
                        'Status': '+' if d.startswith('+') else '-',
                        'Content': d.split(' ', 1)[1]
                    } for d in diff)

        # Create a DataFrame from the differences
        result_df = pd.DataFrame(differences)

        return result_df

    except FileNotFoundError:
        raise FileNotFoundError(f"One or both of the files ({file_path1}, {file_path2}) could not be found.")
    except Exception as e:
        raise Exception(f"An error occurred while processing the files: {e}")