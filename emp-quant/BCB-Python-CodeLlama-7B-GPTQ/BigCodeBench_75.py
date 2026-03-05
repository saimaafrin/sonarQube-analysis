import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns
def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    """
    Appends randomly generated sales data for specified fruits over a given range of days to a DataFrame, and returns a seaborn boxplot of the sales.
    The function should raise the exception for:
        TypeError: If 'df' is not a pandas DataFrame.
        ValueError: If 'df' is not empty or 
                    If 'sales_lower_bound' is not less than 'sales_upper_bound'.
    The function should output with:
        Tuple[pd.DataFrame, sns.axisgrid.FacetGrid]: Updated DataFrame with sales data and a seaborn boxplot of the sales.
    """
    # Check if 'df' is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame")

    # Check if 'df' is not empty
    if df.empty:
        raise ValueError("'df' must not be empty")

    # Check if 'sales_lower_bound' is less than 'sales_upper_bound'
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("'sales_lower_bound' must be less than 'sales_upper_bound'")

    # Generate random sales data for specified fruits over a given range of days
    sales_data = {}
    for fruit in fruits:
        sales_data[fruit] = []
        for day in range(days):
            sales_data[fruit].append(np.random.randint(sales_lower_bound, sales_upper_bound))

    # Append sales data to the DataFrame
    for fruit, sales in sales_data.items():
        df[fruit] = sales

    # Create a seaborn boxplot of the sales
    g = sns.boxplot(data=df, x="fruit", y="sales")

    return df, g
df = pd.DataFrame()
fruits = ["apple", "banana", "orange"]
days = 30
seed = 42
sales_lower_bound = 1
sales_upper_bound = 50