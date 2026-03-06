
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    # Calculate the average of each row
    data_mean = data_scaled.mean(axis=1)

    # Add the average column to the DataFrame
    data_scaled['Average'] = data_mean

    # Visualize the averages in a bar plot
    fig, ax = plt.subplots()
    ax.bar(data_mean.index, data_mean.values)
    ax.set_xlabel('Average')
    ax.set_ylabel('Value')
    ax.set_title('Average of each row')

    return data_scaled, ax