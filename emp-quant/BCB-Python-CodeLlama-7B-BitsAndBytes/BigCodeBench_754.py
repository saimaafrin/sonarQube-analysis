
import numpy as np
import pandas as pd
from datetime import datetime
# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Check if the input contains any "from_user" values
    if len(result['from_user']) == 0:
        return pd.Series([np.nan, np.nan, np.nan, np.nan, np.nan, datetime.now().strftime(DATE_FORMAT)])

    # Convert the "from_user" values to a numpy array
    from_user_array = np.array(result['from_user'])

    # Calculate the mean, median, min, max, and standard deviation of the "from_user" values
    mean = np.mean(from_user_array)
    median = np.median(from_user_array)
    min_value = np.min(from_user_array)
    max_value = np.max(from_user_array)
    std = np.std(from_user_array)

    # Create a pandas Series with the statistical summary
    summary = pd.Series([mean, median, min_value, max_value, std, datetime.now().strftime(DATE_FORMAT)])

    # Raise a ValueError if the "from_user" values are not numeric
    if not np.issubdtype(from_user_array.dtype, np.number):
        raise ValueError("The 'from_user' values must be numeric")

    return summary