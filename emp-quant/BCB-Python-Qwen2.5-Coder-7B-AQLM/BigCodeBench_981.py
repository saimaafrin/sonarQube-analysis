
import pandas as pd
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(start_date, end_date, num_series, seed=None):
    if seed is not None:
        random.seed(seed)
    
    if start_date > end_date:
        raise ValueError("start_date must be earlier than end_date")
    if num_series < 1:
        raise ValueError("num_series must be at least 1")
    
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    date_range = pd.date_range(start=start_date, end=end_date)
    
    data = {f"series_{i+1}": [random.randint(0, 100) for _ in date_range] for i in range(num_series)}
    df = pd.DataFrame(data, index=date_range)
    
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)
    
    plt.title("Random Time Series")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
    
    return df, plt.gca()