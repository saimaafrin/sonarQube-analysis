import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data):
    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Calculate the average of each row
    averages = scaled_data.mean(axis=1)

    # Add the average column to the DataFrame
    data['Average'] = averages

    # Visualize the averages in a bar plot
    fig, ax = plt.subplots()
    ax.bar(range(len(averages)), averages)
    ax.set_xlabel('Index')
    ax.set_ylabel('Average')
    ax.set_title('Average Values')

    return data, ax
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})