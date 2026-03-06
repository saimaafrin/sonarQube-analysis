
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

def task_func(seed=42):
    # Generate random time series data for the past 30 days
    data = []
    for i in range(30):
        data.append(random.randint(10, 20))
    df = pd.DataFrame(data, columns=['Value'])
    df['Date'] = pd.date_range(start=datetime.now() - pd.Timedelta(days=30), periods=30)

    # Plot the data
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Date'], df['Value'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Random Time Series Data')
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_facecolor('white')
    ax.grid(color='gray', linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)

    # Set the font style
    plt.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 12

    return ax