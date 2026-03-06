
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    """
    Draws a pie chart showing the job distribution in the given data.

    Parameters:
    data (pd.DataFrame): A DataFrame containing the job distribution data.

    Returns:
    matplotlib.figure.Figure: The Figure object containing the pie chart.

    Raises:
    ValueError: If the input data is not a DataFrame.
    """

    # Check if the input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a DataFrame.")

    # Extract job distribution data
    job_distribution = data['job'].value_counts()

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(job_distribution, labels=job_distribution.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return fig