import pandas as pd
import matplotlib.pyplot as plt
def task_func(data):
    """
    Draw a pie chart that shows the job distribution in the given data and return the plot object.
    The function should raise ValueError if the input data is not a DataFrame.
    The function should output with:
        matplotlib.figure.Figure: The Figure object containing the pie chart.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    # Calculate the job distribution
    job_counts = data["job"].value_counts()

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(job_counts, labels=job_counts.index, autopct="%1.1f%%")
    ax.set_title("Job Distribution")

    return fig
data = pd.DataFrame({"job": ["A", "B", "C", "A", "B", "C"]})