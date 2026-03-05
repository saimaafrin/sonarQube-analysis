import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    # Combine a list of dictionaries with the same keys into a single dataframe
    df = pd.DataFrame(data)
    
    # Fill NA/NaN values with 0
    df.fillna(0, inplace=True)
    
    # Generate a line chart of sales
    ax = df.plot(kind='line', title='Fruit Sales over Time', xlabel='Time', ylabel='Sales Quantity')
    
    return ax