import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    # Combine the list of dictionaries into a single DataFrame
    df = pd.concat(data, names=['Time', 'Fruit', 'Sales']).unstack(level=1).fillna(0)
    
    # Plot the sales data
    ax = df.plot(kind='line', title='Fruit Sales over Time', xlabel='Time', ylabel='Sales Quantity')
    
    return ax