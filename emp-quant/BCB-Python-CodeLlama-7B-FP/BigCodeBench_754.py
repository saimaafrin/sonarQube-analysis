import numpy as np
import pandas as pd
from datetime import datetime
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Check if the input is a pandas Series
    if not isinstance(result, pd.Series):
        raise ValueError('Input must be a pandas Series')
    # Extract the "from_user" values
    from_user = result['from_user']
    # Check if the "from_user" values are numeric
    if not np.issubdtype(from_user.dtype, np.number):
        raise ValueError('"from_user" values must be numeric')
    # Calculate the statistical summary
    summary = pd.Series({
        'mean': from_user.mean(),
        'median': from_user.median(),
        'min': from_user.min(),
        'max': from_user.max(),
        'std': from_user.std(),
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })
    # Return the summary
    return summary
result = pd.Series({'from_user': [1, 2, 3, 4, 5]})