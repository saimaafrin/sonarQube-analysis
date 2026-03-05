
from collections import Counter
import pandas as pd

def flatten_menu_items(list_of_menuitems):
    """
    Flattens a nested list of menu items and returns a Pandas DataFrame
    detailing the count of each individual menu item with index name 'MenuItem'.
    """
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Create a Counter object to count the number of occurrences of each menu item
    counter = Counter(flat_list)
    
    # Create a Pandas DataFrame with the menu items as indices and the count of each item
    df = pd.DataFrame(counter.items(), columns=['MenuItem', 'Count'])
    
    return df