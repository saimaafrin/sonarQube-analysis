
from collections import Counter
from random import choice, seed
# Constants
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def task_func(list_of_lists):
    # Initialize an empty list to store the shopping carts
    baskets = []
    # Iterate over the list of lists
    for lst in list_of_lists:
        # Initialize a new Counter object for the current list
        basket = Counter()
        # Iterate over the items in the current list
        for item in lst:
            # Randomly select an item from the possible items list
            selected_item = choice(POSSIBLE_ITEMS)
            # Increment the frequency of the selected item in the basket
            basket[selected_item] += 1
        # Add the basket to the list of baskets
        baskets.append(basket)
    return baskets