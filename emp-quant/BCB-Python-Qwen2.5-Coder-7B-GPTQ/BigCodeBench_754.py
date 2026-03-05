import numpy as np
import pandas as pd
from datetime import datetime
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def task_func(result):
    # Extract 'from_user' values from the result
    from_user_values = result.get('from_user', [])
    
    # Initialize statistical values with np.nan
    mean_val = np.nan
    median_val = np.nan
    min_val = np.nan
    max_val = np.nan
    std_val = np.nan
    
    # Check if 'from_user' values are numeric
    if all(isinstance(val, (int, float)) for val in from_user_values):
        # Convert to numpy array for efficient computation
        from_user_array = np.array(from_user_values)
        
        # Calculate statistical values
        mean_val = np.mean(from_user_array)
        median_val = np.median(from_user_array)
        min_val = np.min(from_user_array)
        max_val = np.max(from_user_array)
        std_val = np.std(from_user_array)
    
    # Get current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    
    # Create a pandas Series with the statistical summary
    summary = pd.Series({
        'mean': mean_val,
        'median': median_val,
        'min': min_val,
        'max': max_val,
        'std': std_val,
        'current_time': current_time
    })
    
    return summary