
import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime

def task_func(seed=42):
    try:
        # Set the seed for reproducibility
        random.seed(seed)
        
        # Generate dates for the past 30 days
        dates = [datetime.now() - timedelta(days=i) for i in range(30)]
        
        # Generate random values
        values = [random.random() * 100 for _ in range(30)]
        
        # Create a DataFrame
        df = pd.DataFrame({'Date': dates, 'Value': values})
        
        # Plotting
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['Value'], marker='o')
        
        # Setting labels and title
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_title('Random Time Series Data', fontsize=14)
        
        # Set font to Arial
        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontname('Arial')
        
        return ax
    
    except Exception as e:
        raise ValueError(f"An error occurred while generating the data or plot: {e}")