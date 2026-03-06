
from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Create a Counter object to count the number of occurrences of each menu item
    counter = Counter(flat_list)

    # Create a Pandas DataFrame with the menu items as indices and the count of each item as a column
    df = pd.DataFrame(counter.items(), columns=['MenuItem', 'Count'])

    return df

# Call the function and print the resulting DataFrame
df = task_func(list_of_menuitems)
print(df)