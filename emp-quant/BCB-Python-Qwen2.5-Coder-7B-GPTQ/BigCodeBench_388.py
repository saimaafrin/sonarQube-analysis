import collections
import pandas as pd
def task_func(my_tuple, path_csv_files):
    result = {}
    for file_path in path_csv_files:
        df = pd.read_csv(file_path)
        for column in my_tuple:
            if column in df.columns:
                column_counts = df[column].value_counts().to_dict()
                result[column] = column_counts
    return result