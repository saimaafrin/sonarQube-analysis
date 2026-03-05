from datetime import datetime
import pandas as pd
from itertools import product
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]
def task_func(date_str):
    """
    Generate a Pandas DataFrame containing a series of dates for a predefined list of employees.
    The function should output with:
        DataFrame: A pandas DataFrame with 'Employee' and 'Date' columns, listing the next 10 days for each employee.
    """
    # Create a list of dates for each employee
    dates = [datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=i) for i in range(10)]
    # Create a DataFrame with the dates and employees
    df = pd.DataFrame({"Employee": EMPLOYEES, "Date": dates})
    return df