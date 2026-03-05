
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Combine the list of dictionaries into a single DataFrame
    df = pd.concat([pd.DataFrame(item) for item in data], ignore_index=True)
    
    # Fill NA/NaN values with 0
    df = df.fillna(0)
    
    # Generate a line chart of sales
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Sales Quantity'], marker='o')
    ax.set_title('Fruit Sales over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')
    
    return ax