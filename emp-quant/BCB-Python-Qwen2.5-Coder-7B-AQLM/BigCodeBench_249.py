
import pandas as pd
import random
from sklearn.model_selection import train_test_split

def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    # Generate random floating-point numbers within the specified range
    random_numbers = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    
    # Create a DataFrame with the generated numbers
    data = pd.DataFrame(random_numbers, columns=['Value'])
    
    # Split the data into train and test sets
    train_set, test_set = train_test_split(data, test_size=test_size, random_state=42)
    
    return train_set, test_set