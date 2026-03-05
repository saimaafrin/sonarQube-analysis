
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

def task_func(seed=42):
    # Generate random time series data
    random.seed(seed)
    dates = [datetime.now() - pd.Timedelta(days=i) for i in range(30)]
    values = [random.randint(1, 100) for _ in range(30)]
    data = pd.DataFrame({'Date': dates, 'Value': values})

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Value'], marker='o')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title('Random Time Series Data', fontsize=14)
    ax.set_fontname('Arial')

    # Return the Axes object
    return ax