
import numpy as np
import pandas as pd
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Check if 'from_user' column exists in the result DataFrame
    if 'from_user' not in result.columns:
        return pd.Series({'mean': np.nan, 'median': np.nan, 'min': np.nan, 'max': np.nan, 'std': np.nan, 'current_time': np.nan})
    
    # Extract 'from_user' values
    from_user_values = result['from_user']
    
    # Check if 'from_user' values are numeric
    if not np.issubdtype(from_user_values.dtype, np.number):
        raise ValueError("The 'from_user' values are not numeric.")
    
    # Calculate statistical summary
    mean_value = from_user_values.mean()
    median_value = from_user_values.median()
    min_value = from_user_values.min()
    max_value = from_user_values.max()
    std_value = from_user_values.std()
    
    # Get current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    
    # Create a pandas Series with the statistical summary
    summary = pd.Series({
        'mean': mean_value,
        'median': median_value,
        'min': min_value,
        'max': max_value,
        'std': std_value,
        'current_time': current_time
    })
    
    return summary