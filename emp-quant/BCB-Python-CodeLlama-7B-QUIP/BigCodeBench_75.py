
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

    # Generate random sales data for the specified fruits over the given range of days
    if fruits:
        for fruit in fruits:
            df[fruit] = np.random.randint(sales_lower_bound, sales_upper_bound, size=days)

    # Create a seaborn boxplot of the sales
    fig, ax = sns.boxplot(data=df, x="date", y="sales", hue="fruit")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.set_title("Sales by Fruit")

    return df, fig