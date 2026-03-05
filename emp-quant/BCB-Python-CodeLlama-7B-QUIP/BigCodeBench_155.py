
import pandas as pd
import matplotlib.pyplot as plt
# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
def task_func(data):
    # Compute the average of each row in the data
    averages = data.mean(axis=1)
    # Create a new DataFrame with the original data and the averages
    new_data = pd.concat([data, pd.DataFrame(averages, columns=['Average'])], axis=1)
    # Plot the averages against the row indices
    fig, ax = plt.subplots()
    ax.plot(new_data['Average'])
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average')
    ax.set_title('Average of Each Row')
    return new_data, fig