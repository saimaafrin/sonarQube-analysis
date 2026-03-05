import numpy as np
import pandas as pd
from datetime import datetime
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Extract 'from_user' values and convert to numpy array
    from_user_values = np.array([item['from_user'] for item in result], dtype=object)
    
    # Initialize statistical values
    mean = np.nan
    median = np.nan
    min_val = np.nan
    max_val = np.nan
    std_dev = np.nan
    
    # Check if 'from_user' values are numeric
    if np.issubdtype(from_user_values.dtype, np.number):
        # Calculate statistical values
        mean = np.mean(from_user_values)
        median = np.median(from_user_values)
        min_val = np.min(from_user_values)
        max_val = np.max(from_user_values)
        std_dev = np.std(from_user_values)
    
    # Get current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    
    # Create summary as a pandas Series
    summary = pd.Series({
        'mean': mean,
        'median': median,
        'min': min_val,
        'max': max_val,
        'std': std_dev,
        'current_time': current_time
    })
    
    return summary