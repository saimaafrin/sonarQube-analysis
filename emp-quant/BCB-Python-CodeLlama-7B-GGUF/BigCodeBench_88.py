
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    sales_data = []
    for date in pd.date_range(start_date, end_date):
        sales_data.append({'Date': date, 'Sales': np.random.randint(0, 500)})
    sales_df = pd.DataFrame(sales_data)
    fig, ax = plt.subplots()
    sales_df['Sales'].plot(kind='bar', ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales over Time')
    return sales_df, ax