
from datetime import datetime
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def task_func(date_str):
    # Create a list of dates for each employee
    dates = [datetime.strptime(date_str, "%Y-%m-%d") + datetime.timedelta(days=i) for i in range(10)]

    # Create a DataFrame with the dates for each employee
    df = pd.DataFrame({"Employee": EMPLOYEES, "Date": dates})

    return df

# Call the function and print the output
df = task_func("2022-01-01")
print(df)