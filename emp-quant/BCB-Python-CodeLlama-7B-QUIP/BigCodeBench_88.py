
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    dates = pd.date_range(start_date, end_date)
    sales = np.random.randint(0, 500, len(dates))
    data = pd.DataFrame({'Date': dates, 'Sales': sales})
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Sales'])
    return data, fig