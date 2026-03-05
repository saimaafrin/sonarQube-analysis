import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    """
    Combine a list of dictionaries with the same keys into a single dictionary,
    turn it into a Pandas DataFrame and create a line plot of the data.
    
    Parameters:
    data (list of dict): A list of dictionaries with the same keys.
    
    Returns:
    matplotlib.axes._axes.Axes or None: Axes object of the plot showing 'Data over Time',
    with 'Time' on the x-axis and 'Data Points' on the y-axis.
    If data is empty, return None.
    """
    if not data:
        return None
    
    # Combine the list of dictionaries into a single dictionary
    combined_data = {}
    for item in data:
        for key, value in item.items():
            if key not in combined_data:
                combined_data[key] = []
            combined_data[key].append(value)
    
    # Create a DataFrame from the combined data
    df = pd.DataFrame(combined_data)
    
    # Create a line plot of the data
    ax = df.plot(kind='line', xlabel='Time', ylabel='Data Points', title='Data over Time')
    
    return ax