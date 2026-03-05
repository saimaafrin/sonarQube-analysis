import numpy as np
import pandas as pd
from datetime import datetime, timedelta
def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    sales_data = []
    for day in pd.date_range(start_date, end_date):
        sales_data.append({'Date': day, 'Sales': np.random.randint(0, 500)})
    sales_df = pd.DataFrame(sales_data)
    sales_df.set_index('Date', inplace=True)
    sales_df.plot(kind='line', x='Date', y='Sales')
    return sales_df, sales_df.axes
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 31)