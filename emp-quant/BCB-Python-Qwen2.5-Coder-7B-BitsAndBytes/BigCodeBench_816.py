
from collections import Counter
import random

# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']

def task_func():
    # Generate a random poker hand
    hand = [random.choice(HAND_RANKS) + random.choice(SUITS) for _ in range(5)]
    
    # Count the frequency of each card rank
    rank_count = Counter(card[0] for card in hand)
    
    return hand, rank_count