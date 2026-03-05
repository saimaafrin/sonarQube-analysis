import pandas as pd
import random
from sklearn.model_selection import train_test_split
def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    # Generate a random set of floating-point numbers within the specified range
    random_floats = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    
    # Create a DataFrame with the generated random floats
    df = pd.DataFrame(random_floats, columns=['Value'])
    
    # Split the data into train and test sets based on the given test size
    train_set, test_set = train_test_split(df, test_size=test_size, random_state=42)
    
    return train_set, test_set