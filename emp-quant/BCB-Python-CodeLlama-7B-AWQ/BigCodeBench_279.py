import random
from collections import Counter
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    """
    Draw x random 5-card poker hands from a 52-card pack (without suits) and return the hands along with a counter of the drawn cards.
    The output is random; hence, the returned list will vary with each call.
    """
    # Create a list of 52 cards
    deck = [card for card in CARDS for _ in range(4)]
    # Shuffle the deck
    random.shuffle(deck)
    # Draw x hands
    hands = [deck[i:i+5] for i in range(0, len(deck), 5)]
    # Count the cards
    counter = Counter(hands)
    # Return the hands and the counter
    return hands, counter