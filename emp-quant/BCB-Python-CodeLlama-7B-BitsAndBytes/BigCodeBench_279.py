
import random
from collections import Counter

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def task_func(x=1):
    hands = []
    counter = Counter()
    for _ in range(x):
        hand = []
        for _ in range(5):
            card = random.choice(CARDS)
            hand.append(card)
            counter[card] += 1
        hands.append(hand)
    return hands, counter