
from datetime import datetime, timedelta
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Convert the input date string to a datetime object
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Generate a list of the next 10 days
    dates = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a list of tuples with employee and date combinations
    employee_date_pairs = list(product(EMPLOYEES, dates))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(employee_date_pairs, columns=['Employee', 'Date'])
    
    # Format the 'Date' column to a string
    df['Date'] = df['Date'].dt.strftime("%Y-%m-%d")
    
    return df