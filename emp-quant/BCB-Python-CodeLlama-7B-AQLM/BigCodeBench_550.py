from collections import Counter
import pandas as pd
def task_func(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and returns a Pandas DataFrame
    detailing the count of each individual menu item with index name 'MenuItem'.

    Parameters:
        list_of_menuitems (list): A nested list of menu items.

    Returns:
        DataFrame: A pandas DataFrame with menu items as indices and a 'Count' column showing the count of each menu item.

    Requirements:
        - collections
        - pandas

    Example:
        >>> result = task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        >>> result.loc['Pizza', 'Count']
        2
        >>> result.loc['Coke', 'Count']
        2
    """
    # Flatten the list
    flat_list = [item for sublist in list_of_menuitems for item in sublist]

    # Count the number of times each menu item appears
    menu_item_counts = Counter(flat_list)

    # Create a DataFrame with the counts
    df = pd.DataFrame.from_dict(menu_item_counts, orient='index')

    # Rename the column
    df.columns = ['Count']

    return df