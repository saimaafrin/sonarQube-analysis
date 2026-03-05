from collections import Counter
import pandas as pd
def task_func(list_of_menuitems):
    # Flatten the nested list
    flattened_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Count the occurrences of each menu item
    menu_counts = Counter(flattened_list)
    
    # Create a DataFrame from the counts
    df = pd.DataFrame(list(menu_counts.items()), columns=['MenuItem', 'Count'])
    
    # Set 'MenuItem' as the index
    df.set_index('MenuItem', inplace=True)
    
    return df