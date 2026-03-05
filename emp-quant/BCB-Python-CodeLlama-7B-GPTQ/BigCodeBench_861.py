from collections import Counter
from random import choice, seed
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def task_func(list_of_lists):
    baskets = []
    for lst in list_of_lists:
        basket = Counter()
        for _ in range(len(lst)):
            basket[choice(POSSIBLE_ITEMS)] += 1
        baskets.append(basket)
    return baskets
list_of_lists = [
    ['apple', 'banana', 'cherry'],
    ['date', 'elderberry'],
    ['apple', 'banana', 'cherry', 'date', 'elderberry'],
]