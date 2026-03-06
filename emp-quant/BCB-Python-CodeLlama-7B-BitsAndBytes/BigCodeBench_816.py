
from collections import Counter
import random
# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']
def task_func():
    # Generate a random poker hand
    hand = []
    for i in range(5):
        rank = random.choice(HAND_RANKS)
        suit = random.choice(SUITS)
        hand.append(rank + suit)
    # Count the frequency of each card rank in the hand
    rank_count = Counter(hand)
    return hand, rank_count