import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    data = []
    for i in range(int((end_date - start_date).days) + 1):
        data.append({
            'Date': start_date + timedelta(days=i),
            'Sales': np.random.randint(0, 500)
        })
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Sales over Time')
    return df, ax
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 31)