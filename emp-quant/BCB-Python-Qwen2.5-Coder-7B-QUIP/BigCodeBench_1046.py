
from datetime import datetime, timedelta
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Convert the input date string to a datetime object
    start_date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Generate a list of the next 10 days
    date_range = [start_date + timedelta(days=i) for i in range(10)]
    
    # Create a list of tuples with employee names and dates
    employee_date_pairs = product(EMPLOYEES, date_range)
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(employee_date_pairs, columns=['Employee', 'Date'])
    
    # Return the DataFrame
    return df