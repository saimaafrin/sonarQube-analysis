
from collections import Counter
import random
# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']
def task_func():
    hand = []
    for i in range(5):
        rank = random.choice(HAND_RANKS)
        suit = random.choice(SUITS)
        card = rank + suit
        hand.append(card)
    rank_count = Counter(hand)
    return hand, rank_count

hand, rank_count = task_func()
print(hand)
print(rank_count)