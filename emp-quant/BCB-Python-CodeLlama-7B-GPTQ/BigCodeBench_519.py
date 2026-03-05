import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    # Combine the list of dictionaries into a single pandas dataframe
    df = pd.DataFrame(data)

    # Fill NA/NaN values with 0
    df = df.fillna(0)

    # Generate a line chart of sales
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Sales Quantity'])
    ax.set_title('Fruit Sales over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')

    return ax
data = [
    {'Time': '2022-01-01', 'Apple': 10, 'Banana': 5, 'Orange': 3},
    {'Time': '2022-01-02', 'Apple': 15, 'Banana': 10, 'Orange': 8},
    {'Time': '2022-01-03', 'Apple': 20, 'Banana': 15, 'Orange': 12},
    {'Time': '2022-01-04', 'Apple': 18, 'Banana': 12, 'Orange': 10},
    {'Time': '2022-01-05', 'Apple': 16, 'Banana': 10, 'Orange': 14},
]