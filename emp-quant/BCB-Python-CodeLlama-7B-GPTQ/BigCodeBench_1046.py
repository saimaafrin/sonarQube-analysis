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
    # Convert the date string to a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # Create a list of tuples containing the employee and the next 10 dates
    dates = [(employee, date + datetime.timedelta(days=i)) for i in range(10) for employee in EMPLOYEES]

    # Create a Pandas DataFrame from the list of tuples
    df = pd.DataFrame(dates, columns=["Employee", "Date"])

    # Return the DataFrame
    return df
date_str = "2023-02-21"