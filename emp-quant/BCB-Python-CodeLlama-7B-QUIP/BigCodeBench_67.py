
import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    file_list = [f for f in os.listdir(dir_path) if re.match(pattern, f)]
    file_sizes = [os.path.getsize(os.path.join(dir_path, f)) for f in file_list]
    return pd.DataFrame({'File': file_list, 'Size': file_sizes})