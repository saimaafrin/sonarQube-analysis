from collections import Counter
import pandas as pd
def task_func(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and returns a Pandas DataFrame detailing the count of each individual menu item with index name 'MenuItem'.
    The function should output with:
        DataFrame: A pandas DataFrame with menu items as indices and a 'Count' column showing the count of each menu item.
    """
    # Flatten the list of menu items
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Create a Counter object from the flattened list
    counter = Counter(flat_list)

    # Create a Pandas DataFrame from the Counter object
    df = pd.DataFrame.from_dict(counter, orient='index')

    # Rename the 'Count' column to 'MenuItem'
    df = df.rename(columns={'Count': 'MenuItem'})

    # Sort the DataFrame by 'MenuItem'
    df = df.sort_values(by='MenuItem')

    return df