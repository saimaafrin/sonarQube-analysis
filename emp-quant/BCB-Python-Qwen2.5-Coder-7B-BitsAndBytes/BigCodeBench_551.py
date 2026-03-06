
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def task_func(list_of_menuitems):
    # Flatten the nested list
    flattened_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Count the frequency of each menu item
    item_counts = Counter(flattened_list)
    
    # Check if there are any items to plot
    if not item_counts:
        return None
    
    # Create a DataFrame from the counts
    df = pd.DataFrame(list(item_counts.items()), columns=['Item', 'Frequency'])
    
    # Sort the DataFrame by frequency in descending order
    df = df.sort_values(by='Frequency', ascending=False)
    
    # Create a bar plot using seaborn
    ax = sns.barplot(x='Frequency', y='Item', data=df)
    
    # Set the title and labels
    ax.set_title('Menu Item Frequency')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Menu Item')
    
    # Show the plot
    plt.show()
    
    return ax

ax = task_func(menu_items)
if ax is not None:
    print("Plot generated successfully.")
else:
    print("No items to plot.")