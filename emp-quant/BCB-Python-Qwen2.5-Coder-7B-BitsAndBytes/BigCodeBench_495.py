
import pandas as pd
import numpy as np

def task_func(days, random_seed=0):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Create an index of dates starting from '2023-01-01'
    dates = pd.date_range(start='2023-01-01', periods=days)
    
    # Define the column names
    columns = ['Groceries', 'Entertainment', 'Rent', 'Utilities', 'Miscellaneous']
    
    # Generate random spending data for each category
    data = {col: np.random.randint(0, 101, size=days) for col in columns}
    
    # Create the DataFrame
    spending_report = pd.DataFrame(data, index=dates)
    
    return spending_report