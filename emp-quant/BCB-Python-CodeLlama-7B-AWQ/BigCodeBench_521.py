import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_list):
    """
    Visualizes the scores of students over multiple tests using a line plot.
    The function takes in a list of dictionaries. Each dictionary contains the name of a student (key) and their score (value).
    It combines these dictionaries into a pandas DataFrame and plots a line graph of student scores over tests, where the x-axis represents the test number and the y-axis represents the score.
    Each student's scores are plotted as separate lines. Missing scores are handled by not plotting those specific data points, allowing for discontinuous lines where data is missing.
    The function should output with:
        ax (matplotlib.axes._axes.Axes): The Axes object with the plotted data.
    """
    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Create a line plot of the student scores over tests
    ax = df.plot(kind='line', x='test', y='score')

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
    {'name': 'Alice', 'score': 100},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 85},
]