
from datetime import datetime, timedelta
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Convert the input date string to a datetime object
    start_date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Create a list of dates for the next 10 days
    dates = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a list of employee-date pairs
    employee_dates = list(product(EMPLOYEES, dates))
    
    # Create a DataFrame from the employee-date pairs
    df = pd.DataFrame(employee_dates, columns=['Employee', 'Date'])
    
    return df