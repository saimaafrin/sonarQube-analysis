import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_list):
    # Combine the dictionaries into a pandas DataFrame
    df = pd.DataFrame(data_list)

    # Plot the line graph of student scores over tests
    ax = df.plot(kind='line', x='test', y='score')

    # Set the x-axis label
    ax.set_xlabel('Test Number')

    # Set the y-axis label
    ax.set_ylabel('Score')

    # Set the title
    ax.set_title('Student Scores Over Tests')

    # Return the Axes object with the plotted data
    return ax
data_list = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
    {'name': 'Alice', 'score': 90},
    {'name': 'Bob', 'score': 80},
    {'name': 'Charlie', 'score': 80},
]