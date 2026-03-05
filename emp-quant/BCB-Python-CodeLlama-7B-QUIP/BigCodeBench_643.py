
import re
import pandas as pd
import numpy as np

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def task_func(dataframe, data_pattern=DATA_PATTERN):
    # Create a new DataFrame with the extracted numeric values
    new_dataframe = pd.DataFrame(dataframe.apply(lambda x: re.search(data_pattern, x).group(0) if re.search(data_pattern, x) else np.nan))
    return new_dataframe