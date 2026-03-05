from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flattened_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Count the frequency of each menu item
    item_counts = Counter(flattened_list)
    
    # Create a DataFrame from the counts
    df = pd.DataFrame(list(item_counts.items()), columns=['Menu Item', 'Frequency'])
    
    # Create a bar plot using seaborn
    if not df.empty:
        ax = sns.barplot(x='Menu Item', y='Frequency', data=df)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return ax
    else:
        return None