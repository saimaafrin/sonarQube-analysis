
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

def task_func(seed=42):
    try:
        # Set the seed for reproducibility
        random.seed(seed)
        
        # Generate dates for the past 30 days
        dates = pd.date_range(start=datetime.now() - pd.Timedelta(days=30), periods=30)
        
        # Generate random values for the time series
        values = [random.randint(0, 100) for _ in range(30)]
        
        # Create a DataFrame
        df = pd.DataFrame({'Date': dates, 'Value': values})
        
        # Set the font to Arial
        plt.rcParams['font.family'] = 'Arial'
        
        # Create the plot
        ax = df.plot(x='Date', y='Value', kind='line')
        
        # Set the labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Random Time Series Data')
        
        return ax
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")