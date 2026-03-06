
import pandas as pd
import random
from scipy import stats

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Generate random dataset
    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['values'])
    
    # Calculate mean, median, and mode
    mean_value = df['values'].mean()
    median_value = df['values'].median()
    mode_value = df['values'].mode()[0]  # Mode can be multiple, we take the first one
    
    # Return results in a dictionary
    return {
        'mean': round(mean_value, 3),
        'median': round(median_value, 3),
        'mode': round(mode_value, 3)
    }