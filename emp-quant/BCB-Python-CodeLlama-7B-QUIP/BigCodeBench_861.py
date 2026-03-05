
from collections import Counter
from random import choice, seed
# Constants
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def task_func(list_of_lists):
    # Initialize the baskets list
    baskets = []
    # Loop through the list of lists and create a counter for each
    for lst in list_of_lists:
        # Create a counter for the current list
        counter = Counter(POSSIBLE_ITEMS)
        # Randomly select an item from the counter and add it to the basket
        basket.append(choice(counter))
    return baskets