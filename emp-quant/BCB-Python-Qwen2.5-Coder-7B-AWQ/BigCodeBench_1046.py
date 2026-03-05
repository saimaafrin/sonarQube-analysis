from datetime import datetime, timedelta
import pandas as pd
from itertools import product
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]
def task_func(date_str):
    # Convert the input date string to a datetime object
    start_date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Generate a list of the next 10 days
    dates = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a list of tuples with employee names and corresponding dates
    data = list(product(EMPLOYEES, dates))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Employee', 'Date'])
    
    # Format the 'Date' column to a string
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    
    return df