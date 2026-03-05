
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Combine the list of dictionaries into a single DataFrame
    df = pd.DataFrame(data)
    
    # Fill NA/NaN values with 0
    df.fillna(0, inplace=True)
    
    # Generate a line chart of sales
    ax = df.plot(kind='line', title='Fruit Sales over Time', x='Time', y='Sales Quantity')
    
    # Set labels for x-axis and y-axis
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')
    
    return ax