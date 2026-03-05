
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    # Create a DataFrame from the given data
    df = pd.DataFrame(data)

    # Create a bar chart for the given column
    ax = df[column].value_counts().plot(kind='bar', rotatelabels=True, figsize=(10, 6))

    # Set the x and y labels
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    # Set the title
    ax.set_title(f'Distribution of {column}')

    # Return the Axes object for the generated plot
    return ax