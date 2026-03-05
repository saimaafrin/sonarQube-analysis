
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    date_range = pd.date_range(start=start_date, end=end_date)
    sales_data = np.random.randint(0, 501, size=len(date_range))
    df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})
    
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return df, ax