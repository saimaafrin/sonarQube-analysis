import pandas as pd
import matplotlib.pyplot as plt
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
def task_func(data):
    # Compute the average of each row in the data
    row_averages = data.mean(axis=1)

    # Create a new DataFrame with the original data and the average column
    data['Average'] = row_averages

    # Plot the row averages against their respective row indices
    fig, ax = plt.subplots()
    ax.plot(data.index, row_averages)
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average')
    ax.set_title('Row Averages')

    return data, ax
data = pd.DataFrame(
    [[1, 2, 3, 4, 5, 6, 7, 8],
     [2, 4, 6, 8, 10, 12, 14, 16],
     [3, 6, 9, 12, 15, 18, 21, 24]],
    columns=COLUMN_NAMES
)