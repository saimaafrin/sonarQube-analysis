
import numpy as np
import pandas as pd
from datetime import datetime
# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Check if there are 'from_user' values in the result
    if 'from_user' not in result:
        raise ValueError("No 'from_user' values found in the result.")
    
    # Extract 'from_user' values and convert to numpy array
    from_user_values = result['from_user']
    if not np.issubdtype(from_user_values.dtype, np.number):
        raise ValueError("The 'from_user' values are not numeric.")
    
    # Calculate statistical summary
    summary = {
        'mean': np.mean(from_user_values),
        'median': np.median(from_user_values),
        'min': np.min(from_user_values),
        'max': np.max(from_user_values),
        'std': np.std(from_user_values)
    }
    
    # Add current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    summary['current_time'] = current_time
    
    # Convert to pandas Series
    result_series = pd.Series(summary)
    
    return result_series