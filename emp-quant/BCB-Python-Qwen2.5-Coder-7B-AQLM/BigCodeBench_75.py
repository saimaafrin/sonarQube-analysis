
import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if not df.empty:
        raise ValueError("df must be empty")
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("sales_lower_bound must be less than sales_upper_bound")
    
    if fruits is None:
        fruits = ['apple', 'banana', 'orange']
    if days is None:
        days = 30
    
    if seed is not None:
        np.random.seed(seed)
    
    date_range = pd.date_range(start=datetime.now(), periods=days)
    fruit_combinations = list(itertools.product(fruits, date_range))
    
    sales_data = []
    for fruit, date in fruit_combinations:
        sales = np.random.randint(sales_lower_bound, sales_upper_bound)
        sales_data.append({'fruit': fruit, 'date': date, 'sales': sales})
    
    new_df = pd.DataFrame(sales_data)
    df = pd.concat([df, new_df], ignore_index=True)
    
    boxplot = sns.boxplot(x='fruit', y='sales', data=df)
    return df, boxplot