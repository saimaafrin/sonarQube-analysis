
from collections import Counter
from random import choice, seed

# Constants
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def task_func(list_of_lists):
    baskets = []
    for lst in list_of_lists:
        basket = Counter()
        for _ in range(len(lst)):
            item = choice(POSSIBLE_ITEMS)
            basket[item] += 1
        baskets.append(basket)
    return baskets