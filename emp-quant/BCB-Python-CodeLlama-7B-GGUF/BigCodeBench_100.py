
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

def task_func(seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Generate random time series data for the past 30 days
    data = []
    for i in range(30):
        data.append(random.uniform(0, 100))

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['Value'])
    df['Date'] = pd.date_range(start=datetime.now() - pd.Timedelta(days=30), periods=30, freq='D')

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Value'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.set_title('Random Time Series Data')
    ax.set_facecolor('white')
    ax.tick_params(axis='x', labelrotation=45)
    ax.grid(True)

    # Set the font to Arial
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontname('Arial')

    return ax