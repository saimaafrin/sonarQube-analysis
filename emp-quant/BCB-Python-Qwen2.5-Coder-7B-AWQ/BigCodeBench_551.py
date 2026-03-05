from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def task_func(list_of_menuitems):
    # Flatten the nested list
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Count the frequency of each menu item
    item_counter = Counter(flat_list)
    
    # Check if there are items to plot
    if not item_counter:
        return None
    
    # Create a DataFrame from the counter
    df = pd.DataFrame(list(item_counter.items()), columns=['Menu Item', 'Frequency'])
    
    # Create a bar plot using seaborn
    ax = sns.barplot(x='Menu Item', y='Frequency', data=df)
    
    # Set the title and labels
    ax.set_title('Frequency of Menu Items')
    ax.set_xlabel('Menu Item')
    ax.set_ylabel('Frequency')
    
    # Return the Axes object
    return ax