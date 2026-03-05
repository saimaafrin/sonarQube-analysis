
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Create a pandas dataframe from the list of dictionaries
    df = pd.DataFrame(data)

    # Fill NA/NaN values with 0
    df = df.fillna(0)

    # Group the dataframe by fruit and calculate the sum of sales
    df_sum = df.groupby('fruit').sum()

    # Convert the dataframe to a line chart
    fig, ax = plt.subplots()
    ax.plot(df_sum['time'], df_sum['sales'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Sales Quantity')
    ax.set_title('Fruit Sales over Time')

    return ax