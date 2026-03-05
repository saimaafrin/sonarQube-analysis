
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Compute the average of each row
    row_averages = data.mean(axis=1)

    # Create a new DataFrame with the original data and the average
    data_with_average = pd.concat([data, pd.DataFrame(row_averages, columns=['Average'])], axis=1)

    # Plot the averages against their respective row indices
    fig, ax = plt.subplots()
    ax.plot(data_with_average.index, data_with_average['Average'])
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average')
    ax.set_title('Row Averages')

    return data_with_average, ax

data_with_average, ax = task_func(data)

print(data_with_average)