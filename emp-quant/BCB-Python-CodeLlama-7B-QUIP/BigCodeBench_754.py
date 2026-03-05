
import numpy as np
import pandas as pd
from datetime import datetime
# Constants
DATE_FORMENTRY_USER_VALUES = 'from_user'
def task_func(result):
    # Calculate the mean, median, min, max, and standard deviation of the "from_user" values
    mean = np.mean(result[ENTRY_USER_VALUES])
    median = np.median(result[ENTRY_USER_VALUES])
    min = np.min(result[ENTRY_USER_VALUES])
    max = np.max(result[ENTRY_USER_VALUES])
    std = np.std(result[ENTRY_USER_VALUES])
    # Add the current date and time to the summary
    current_time = datetime.now().strftime(DATE_FORMENTRY_USER_VALUES)
    summary = pd.Series([
        'mean': mean,
        'median': median,
        'min': min,
        'max': max,
        'std': std,
        'current_time': current_time
    ])
    return summary