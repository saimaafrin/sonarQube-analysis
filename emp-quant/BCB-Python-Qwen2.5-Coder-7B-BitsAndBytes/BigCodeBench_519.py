
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Combine list of dictionaries into a DataFrame
    df = pd.DataFrame(data)
    
    # Fill NaN values with 0
    df.fillna(0, inplace=True)
    
    # Generate a line chart
    ax = df.plot(kind='line')
    
    # Set the title and labels
    ax.set_title('Fruit Sales over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')
    
    return ax