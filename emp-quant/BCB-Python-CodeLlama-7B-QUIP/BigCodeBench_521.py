
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_list):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Group the DataFrame by student name
    df_grouped = df.groupby("name")

    # Create a line plot for each student
    ax = plt.figure(figsize=(8,6))
    for name, group in df_grouped:
        ax.plot(group["test_number"], group["score"])

    # Set the x-axis and y-axis labels
    ax.set_xlabel("Test Number")
    ax.set_ylabel("Score")

    # Return the Axes object
    return ax