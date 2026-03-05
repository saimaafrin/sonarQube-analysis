
from collections import Counter
from random import choice, seed
# Constants
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def task_func(list_of_lists):
    baskets = []
    seed(42)  # For reproducibility
    for lst in list_of_lists:
        cart = Counter(choice(POSSIBLE_ITEMS) for _ in range(len(lst)))
        baskets.append(cart)
    return baskets