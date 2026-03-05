
import numpy as np
import pandas as pd
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Check if 'from_user' column exists
    if 'from_user' not in result:
        return pd.Series({'mean': np.nan, 'median': np.nan, 'min': np.nan, 'max': np.nan, 'std': np.nan, 'current_time': np.nan})
    
    # Convert 'from_user' column to numeric, raising ValueError if not possible
    try:
        result['from_user'] = pd.to_numeric(result['from_user'], errors='raise')
    except ValueError:
        raise ValueError("The 'from_user' values are not numeric.")
    
    # Calculate statistical summary
    summary = pd.Series({
        'mean': result['from_user'].mean(),
        'median': result['from_user'].median(),
        'min': result['from_user'].min(),
        'max': result['from_user'].max(),
        'std': result['from_user'].std()
    })
    
    # Add current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    summary['current_time'] = current_time
    
    return summary