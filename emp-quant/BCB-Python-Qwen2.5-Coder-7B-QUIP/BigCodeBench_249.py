
import pandas as pd
import random
from sklearn.model_selection import train_test_split

def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    # Generate a random set of floating-point numbers within a specified range
    data = pd.DataFrame({'Value': [random.uniform(min_value, max_value) for _ in range(n_data_points)]})
    
    # Truncate each value to 3 decimal places
    data['Value'] = data['Value'].round(3)
    
    # Divide the data into train and test sets
    train_set, test_set = train_test_split(data, test_size=test_size, random_state=42)
    
    return (train_set, test_set)