import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and visualize the data using a bar chart.
    
    Parameters:
    list_of_pairs (list of tuples): A list where each tuple contains two elements, a category and a value.
    
    Returns:
    tuple:
    - DataFrame: A pandas DataFrame with columns 'Category' and 'Value'.
    - Axes: A matplotlib Axes displaying a bar chart of categories vs. values.
    """
    # Create DataFrame from list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    
    # Create a bar chart
    ax = sns.barplot(x='Category', y='Value', data=df)
    ax.set_title('Category vs Value')
    
    return df, ax