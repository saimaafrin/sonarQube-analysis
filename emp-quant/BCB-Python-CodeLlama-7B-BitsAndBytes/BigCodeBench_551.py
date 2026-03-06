
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Create a Counter object to count the frequency of each menu item
    counter = Counter(flat_list)

    # Create a DataFrame from the Counter object
    df = pd.DataFrame(counter.items(), columns=['Menu Item', 'Frequency'])

    # Sort the DataFrame by frequency
    df.sort_values(by='Frequency', ascending=False, inplace=True)

    # Create a barplot using Seaborn
    ax = sns.barplot(x='Menu Item', y='Frequency', data=df)

    # Return the Axes object
    return ax