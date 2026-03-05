
from datetime import datetime
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Convert date string to datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # Generate list of dates for each employee
    dates = [date + timedelta(days=i) for i in range(10)]

    # Create DataFrame with Employee and Date columns
    df = pd.DataFrame({"Employee": EMPLOYEES, "Date": dates})

    return df