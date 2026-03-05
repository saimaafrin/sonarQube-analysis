
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Calculate the average of each row
    averages = normalized_data.mean(axis=1)

    # Add the averages as a new column to the DataFrame
    data['Average'] = averages

    # Visualize the averages in a bar plot
    fig, ax = plt.subplots()
    ax.bar(range(len(averages)), averages)
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average')
    ax.set_title('Averages')
    plt.show()

    return data