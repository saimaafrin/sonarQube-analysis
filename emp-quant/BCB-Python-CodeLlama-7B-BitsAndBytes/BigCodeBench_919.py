
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    # Create a new DataFrame with the specified column
    df = pd.DataFrame(data, columns=[column])

    # Create a new figure and axis object
    fig, ax = plt.subplots()

    # Create a bar plot of the distribution of categories in the specified column
    ax.bar(df[column].value_counts().index, df[column].value_counts().values)

    # Set the x label and y label of the plot
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    # Set the title of the plot
    ax.set_title(f'Distribution of {column}')

    # Return the Axes object for the generated plot
    return ax