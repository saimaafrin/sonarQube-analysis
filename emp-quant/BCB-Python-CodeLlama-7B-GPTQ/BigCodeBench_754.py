import numpy as np
import pandas as pd
from datetime import datetime
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    """
    Calculate the mean, median, min, max, and standard deviation of the "from_user" values in "result" and add the current date and time in the format YYYY-mm-dd HHL:MM:SS to the summary.
    The global constant DATE_FORMAT is used to transform the currnet date and time into this format.
    Data Structures:
    - Uses numpy arrays for efficient statistical computations.
    """
    # Check if the input contains any "from_user" values
    if result['from_user'].size == 0:
        return pd.Series({
            'mean': np.nan,
            'median': np.nan,
            'min': np.nan,
            'max': np.nan,
            'std': np.nan,
            'current_time': datetime.now().strftime(DATE_FORMAT)
        })

    # Check if the "from_user" values are numeric
    if not np.issubdtype(result['from_user'].dtype, np.number):
        raise ValueError('The "from_user" values must be numeric')

    # Calculate the statistical summary
    summary = pd.Series({
        'mean': result['from_user'].mean(),
        'median': result['from_user'].median(),
        'min': result['from_user'].min(),
        'max': result['from_user'].max(),
        'std': result['from_user'].std(),
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })

    return summary
result = pd.DataFrame({
    'from_user': [1, 2, 3, 4, 5],
    'to_user': [6, 7, 8, 9, 10]
})