
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame")

    # Create a pie chart with the job distribution
    fig, ax = plt.subplots()
    ax.pie(data['Job'], labels=data['Job'], autopct='%1.1f%%')
    ax.set_title('Job Distribution')

    return fig