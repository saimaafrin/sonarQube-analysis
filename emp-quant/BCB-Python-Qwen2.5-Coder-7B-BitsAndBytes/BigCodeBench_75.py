
import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def task_func(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input 'df' must be a pandas DataFrame.")
    
    if not df.empty:
        raise ValueError("Input 'df' must be an empty DataFrame.")
    
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("'sales_lower_bound' must be less than 'sales_upper_bound'.")
    
    if fruits is None:
        fruits = ['Apple', 'Banana', 'Cherry']
    
    if days is None:
        days = 30
    
    if seed is not None:
        np.random.seed(seed)
    
    date_range = [datetime.now() - timedelta(days=i) for i in range(days)]
    fruit_combinations = list(itertools.product(fruits, repeat=days))
    
    sales_data = []
    for date, combination in zip(date_range, fruit_combinations):
        for fruit, sales in zip(combination, np.random.randint(sales_lower_bound, sales_upper_bound, size=len(fruits))):
            sales_data.append({'Date': date, 'Fruit': fruit, 'Sales': sales})
    
    new_df = pd.DataFrame(sales_data)
    df = pd.concat([df, new_df], ignore_index=True)
    
    boxplot = sns.boxplot(x='Fruit', y='Sales', data=df)
    return df, boxplot