from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def task_func(list_of_menuitems):
    # Flatten the nested list
    flattened_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Count the frequency of each menu item
    item_counts = Counter(flattened_list)
    
    # Create a DataFrame for seaborn plotting
    df = pd.DataFrame(list(item_counts.items()), columns=['Item', 'Frequency'])
    
    # Check if there are items to plot
    if df.empty:
        return None
    
    # Create a barplot using seaborn
    ax = sns.barplot(x='Item', y='Frequency', data=df)
    
    # Set the title and labels
    ax.set_title('Frequency of Menu Items')
    ax.set_xlabel('Menu Item')
    ax.set_ylabel('Frequency')
    
    # Rotate x-axis labels for better readability
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    # Return the Axes object
    return ax