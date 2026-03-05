
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a DataFrame")

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(data['Job'], labels=data['Job'])
    ax.set_title("Job Distribution")
    ax.set_ylabel("Count")
    ax.set_xlabel("Job")
    ax.set_ylabel("Count")
    plt.show()

    return fig