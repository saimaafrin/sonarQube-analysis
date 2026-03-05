
from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    
    # Create a Counter object to count the frequency of each menu item
    counter = Counter(flat_list)
    
    # Convert the Counter object to a DataFrame
    df = pd.DataFrame(counter.items(), columns=['MenuItem', 'Count'])
    
    return df