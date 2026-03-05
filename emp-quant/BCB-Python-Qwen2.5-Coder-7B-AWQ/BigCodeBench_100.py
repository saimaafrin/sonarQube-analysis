import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime
def task_func(seed=42):
    try:
        # Set the seed for reproducibility
        random.seed(seed)
        
        # Generate dates for the past 30 days
        dates = [datetime.now() - pd.Timedelta(days=i) for i in range(30)]
        
        # Generate random values
        values = [random.randint(0, 100) for _ in range(30)]
        
        # Create a DataFrame
        df = pd.DataFrame({'Date': dates, 'Value': values})
        
        # Set the date column as the index
        df.set_index('Date', inplace=True)
        
        # Create a line plot
        ax = df.plot(kind='line', figsize=(10, 5))
        
        # Set the plot title and labels
        ax.set_title('Random Time Series Data')
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        
        # Set the font to Arial
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontname('Arial')
        
        return ax
    
    except Exception as e:
        raise ValueError(f"An error occurred: {e}")