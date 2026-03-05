
import numpy as np
import pandas as pd
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Check if 'from_user' column exists in the result
    if 'from_user' not in result:
        return pd.Series({'mean': np.nan, 'median': np.nan, 'min': np.nan, 'max': np.nan, 'std': np.nan, 'current_time': np.nan})
    
    # Extract 'from_user' values
    from_user_values = result['from_user']
    
    # Check if 'from_user' values are numeric
    if not np.issubdtype(from_user_values.dtype, np.number):
        raise ValueError("The 'from_user' values are not numeric.")
    
    # Calculate statistical summary
    mean = np.mean(from_user_values)
    median = np.median(from_user_values)
    min_val = np.min(from_user_values)
    max_val = np.max(from_user_values)
    std_dev = np.std(from_user_values)
    
    # Get current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    
    # Create and return the summary Series
    summary = pd.Series({
        'mean': mean,
        'median': median,
        'min': min_val,
        'max': max_val,
        'std': std_dev,
        'current_time': current_time
    })
    
    return summary