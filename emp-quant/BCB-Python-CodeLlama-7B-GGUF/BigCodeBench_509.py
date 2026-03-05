
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    """
    Compare two CSV files and create a difference report.

    Parameters
    ----------
    file_path1 : str
        Path to the first CSV file.
    file_path2 : str
        Path to the second CSV file.
    delimiter : str, optional
        Delimiter used in the CSV files. Defaults to ','.
    quotechar : str, optional
        Quote character used in the CSV files. Defaults to '"'.

    Returns
    -------
    DataFrame
        A pandas DataFrame with the differences.

    Raises
    ------
    FileNotFoundError
        If either of the files cannot be found.
    ValueError
        If either of the files is empty.
    Exception
        For other IO related errors.
    """
    try:
        with open(file_path1, 'r', newline='') as f1, open(file_path2, 'r', newline='') as f2:
            reader1 = csv.reader(f1, delimiter=delimiter, quotechar=quotechar)
            reader2 = csv.reader(f2, delimiter=delimiter, quotechar=quotechar)

            # Create a list of tuples containing the line number and the line content
            lines1 = [(i + 1, line) for i, line in enumerate(reader1)]
            lines2 = [(i + 1, line) for i, line in enumerate(reader2)]

            # Create a list of tuples containing the line number, status, and content
            differences = [(i + 1, ' ', line) for i, line in enumerate(lines1) if line not in lines2]
            differences += [(i + 1, '+', line) for i, line in enumerate(lines2) if line not in lines1]
            differences += [(i + 1, '-', line) for i, line in enumerate(lines1) if line not in lines2]

            # Create a DataFrame with the differences
            df = pd.DataFrame(differences, columns=['Line Number', 'Status', 'Content'])

            return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path1} or {file_path2} not found.")
    except ValueError:
        raise ValueError(f"File {file_path1} or {file_path2} is empty.")
    except Exception as e:
        raise Exception(f"Error reading files: {e}")