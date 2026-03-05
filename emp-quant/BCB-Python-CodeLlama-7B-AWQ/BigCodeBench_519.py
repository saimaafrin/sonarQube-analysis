import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    # Combine the list of dictionaries into a single pandas dataframe
    df = pd.DataFrame(data)

    # Fill NA/NaN values with 0
    df = df.fillna(0)

    # Generate a line chart of sales
    ax = df.plot(kind='line', x='Time', y='Sales Quantity', title='Fruit Sales over Time')

    # Set the x-axis label
    ax.set_xlabel('Time')

    # Set the y-axis label
    ax.set_ylabel('Sales Quantity')

    # Return the Axes object
    return ax
data = [
    {'Time': '2022-01-01', 'Apple': 100, 'Banana': 50, 'Orange': 20},
    {'Time': '2022-01-02', 'Apple': 150, 'Banana': 60, 'Orange': 30},
    {'Time': '2022-01-03', 'Apple': 120, 'Banana': 70, 'Orange': 40},
    {'Time': '2022-01-04', 'Apple': 180, 'Banana': 80, 'Orange': 50},
    {'Time': '2022-01-05', 'Apple': 200, 'Banana': 90, 'Orange': 60},
]