from collections import Counter
from random import choice, seed
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def task_func(list_of_lists):
    baskets = []
    seed(42)  # Seed for reproducibility
    for lst in list_of_lists:
        cart = Counter()
        for _ in range(len(lst)):
            item = choice(POSSIBLE_ITEMS)
            cart[item] += 1
        baskets.append(cart)
    return baskets
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]