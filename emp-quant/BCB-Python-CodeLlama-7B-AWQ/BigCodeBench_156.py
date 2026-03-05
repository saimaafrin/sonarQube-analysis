import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data):
    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    # Calculate the average of each row
    data_average = data_scaled.mean(axis=1)

    # Add the average column to the DataFrame
    data_average = pd.DataFrame(data_average, columns=['Average'])
    data_scaled = pd.concat([data_scaled, data_average], axis=1)

    # Visualize the averages in a bar plot
    fig, ax = plt.subplots()
    ax.bar(data_average.index, data_average['Average'])
    ax.set_xlabel('Index')
    ax.set_ylabel('Average')
    ax.set_title('Average of each row')
    plt.show()

    return data_scaled, ax
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})