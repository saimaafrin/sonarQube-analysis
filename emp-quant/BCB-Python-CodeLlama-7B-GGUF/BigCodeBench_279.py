
import random
from collections import Counter
# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    # Generate x random 5-card hands
    hands = [random.sample(CARDS, 5) for _ in range(x)]
    # Count the drawn cards
    counter = Counter(card for hand in hands for card in hand)
    return hands, counter