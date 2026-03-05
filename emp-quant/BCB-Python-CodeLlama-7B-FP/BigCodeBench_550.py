from collections import Counter
import pandas as pd
def task_func(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and returns a Pandas DataFrame detailing the count of each individual menu item with index name 'MenuItem'.
    """
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Create a Counter object to count the number of occurrences of each menu item
    counter = Counter(flat_list)

    # Create a Pandas DataFrame with the counts of each menu item
    df = pd.DataFrame(counter.most_common(), columns=['MenuItem', 'Count'])

    # Set the index of the DataFrame to 'MenuItem'
    df.set_index('MenuItem', inplace=True)

    return df
list_of_menuitems = [
    ['Item 1', 'Item 2', 'Item 3'],
    ['Item 1', 'Item 2', 'Item 4'],
    ['Item 1', 'Item 5', 'Item 6'],
]