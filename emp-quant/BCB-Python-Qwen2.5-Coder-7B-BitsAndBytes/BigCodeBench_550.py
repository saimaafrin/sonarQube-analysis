
from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    # Flatten the nested list
    flattened_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Count the occurrences of each menu item
    item_counts = Counter(flattened_list)
    
    # Create a DataFrame from the counts
    df = pd.DataFrame(item_counts.items(), columns=['MenuItem', 'Count'])
    
    return df

result_df = task_func(nested_menu_items)
print(result_df)