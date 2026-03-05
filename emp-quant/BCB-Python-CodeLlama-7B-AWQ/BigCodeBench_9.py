import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and visualize the data using a bar chart.
    The title of the barplot should be set to 'Category vs Value'.
    """
    # Create a Pandas DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    # Visualize the data using a bar chart
    ax = sns.barplot(x='Category', y='Value', data=df)
    ax.set_title('Category vs Value')

    return df, ax
list_of_pairs = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]