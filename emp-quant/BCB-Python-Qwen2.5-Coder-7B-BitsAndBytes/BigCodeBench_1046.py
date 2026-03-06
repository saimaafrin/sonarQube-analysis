
from datetime import datetime, timedelta
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Convert input date string to datetime object
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Generate a list of dates for the next 10 days
    dates = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a list of tuples with employee names and corresponding dates
    data = list(product(EMPLOYEES, dates))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Employee', 'Date'])
    
    return df