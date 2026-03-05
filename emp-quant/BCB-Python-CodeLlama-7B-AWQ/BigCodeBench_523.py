import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    """
    Combine a list of dictionaries with the same keys into a single dictionary, turn it into a Pandas DataFrame and create a line plot of the data.
    The function should output with:
        matplotlib.axes._axes.Axes or None: Axes object of the plot showing 'Data over Time',
        with 'Time' on the x-axis and 'Data Points' on the y-axis.
        If data is empty, return None.
    """
    # Check if data is empty
    if not data:
        return None

    # Combine the dictionaries into a single dictionary
    combined_dict = {}
    for d in data:
        for k, v in d.items():
            if k not in combined_dict:
                combined_dict[k] = []
            combined_dict[k].append(v)

    # Create a Pandas DataFrame from the combined dictionary
    df = pd.DataFrame(combined_dict)

    # Create a line plot of the data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Data Points'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Data Points')
    ax.set_title('Data over Time')
    return ax
data = [
    {'Time': 1, 'Data Points': 10},
    {'Time': 2, 'Data Points': 20},
    {'Time': 3, 'Data Points': 30},
    {'Time': 4, 'Data Points': 40},
    {'Time': 5, 'Data Points': 50},
]