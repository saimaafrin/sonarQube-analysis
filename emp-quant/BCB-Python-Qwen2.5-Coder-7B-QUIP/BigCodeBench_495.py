
import pandas as pd
import numpy as np

def task_func(days, random_seed=0):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Define the start date
    start_date = '2023-01-01'
    
    # Create a date range for the specified number of days
    date_range = pd.date_range(start=start_date, periods=days, freq='D')
    
    # Define the columns for the DataFrame
    columns = ['Groceries', 'Entertainment', 'Rent', 'Utilities', 'Miscellaneous']
    
    # Create a DataFrame with random values for each column
    data = np.random.randint(0, 101, size=(days, len(columns)))
    
    # Create a DataFrame with the date range as the index
    df = pd.DataFrame(data, index=date_range, columns=columns)
    
    return df