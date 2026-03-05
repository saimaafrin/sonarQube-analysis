import pandas as pd
import random
from scipy import stats
def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Generate a random dataset of floating-point numbers within a specified range
    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    
    # Convert the list to a pandas DataFrame
    df = pd.DataFrame(data, columns=['values'])
    
    # Calculate statistical measures
    mean = df['values'].mean()
    median = df['values'].median()
    mode = df['values'].mode()[0]  # Get the first mode if there are multiple
    
    # Return the results in a dictionary
    return {'mean': mean, 'median': median, 'mode': mode}