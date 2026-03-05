
import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("'df' must be a pandas DataFrame")
    if df.empty:
        raise ValueError("'df' must not be empty")
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("'sales_lower_bound' must be less than 'sales_upper_bound'")

    # Generate random sales data for each fruit over the specified range of days
    sales_data = {}
    for fruit in fruits:
        sales_data[fruit] = []
        for day in range(days):
            sales_data[fruit].append(np.random.randint(sales_lower_bound, sales_upper_bound))

    # Create a new DataFrame with the sales data
    sales_df = pd.DataFrame(sales_data, index=pd.date_range(start=datetime.now(), periods=days, freq='D'))

    # Create a seaborn boxplot of the sales
    g = sns.boxplot(data=sales_df, orient="v", width=0.5)

    return sales_df, g