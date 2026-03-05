
import numpy as np
import pandas as pd
from datetime import datetime
# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Check if "from_user" values are numeric
    if not np.issubdtype(result['from_user'].dtype, np.number):
        raise ValueError("'from_user' values must be numeric")
    # Calculate statistical summary
    summary = pd.Series({
        'mean': result['from_user'].mean(),
        'median': result['from_user'].median(),
        'min': result['from_user'].min(),
        'max': result['from_user'].max(),
        'std': result['from_user'].std(),
        'current_time': datetime.now().strftime(DATE_FORMAT)
    })
    # Return summary
    return summary