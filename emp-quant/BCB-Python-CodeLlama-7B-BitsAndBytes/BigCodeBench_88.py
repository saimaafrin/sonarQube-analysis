
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    dates = pd.date_range(start_date, end_date)
    sales = np.random.randint(0, 500, len(dates))
    df = pd.DataFrame({'Date': dates, 'Sales': sales})
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales over Time')
    return df, fig