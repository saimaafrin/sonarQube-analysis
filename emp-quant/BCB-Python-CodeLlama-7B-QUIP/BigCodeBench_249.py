
import pandas as pd
import random
from sklearn.model_selection import train_test_split

def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    # Generate a random set of floating-point numbers within the specified range
    data = random.uniform(min_value, max_value, n_data_points)

    # Truncate each value to 3 decimal places
    data = data.round(3)

    # Divide the data into train and test sets based on the specified test size
    train_data, test_data = train_test_split(data, test_size=test_size)

    # Create a pandas DataFrame for the train and test sets
    train_df = pd.DataFrame({'Value': train_data})
    test_df = pd.DataFrame({'Value': test_data})

    return (train_df, test_df)