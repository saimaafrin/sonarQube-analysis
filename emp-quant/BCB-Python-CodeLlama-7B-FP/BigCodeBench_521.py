import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_list):
    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Plot the line graph of student scores over tests
    ax = df.plot(kind='line', x='test', y='score', legend=False)

    # Set the x-axis label and y-axis label
    ax.set_xlabel('Test Number')
    ax.set_ylabel('Score')

    # Return the Axes object with the plotted data
    return ax
data_list = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 85},
    {'name': 'Charlie', 'score': 80},
]