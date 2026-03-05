import random
from collections import Counter
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    """
    Draw x random 5-card poker hands from a 52-card pack (without suits) and return the hands along with a counter of the drawn cards.
    The output is random; hence, the returned list will vary with each call.
    """
    # Initialize a list to store the drawn cards
    drawn_cards = []
    # Initialize a counter to count the number of drawn cards
    counter = Counter()

    # Draw x random 5-card poker hands
    for _ in range(x):
        # Generate a random 5-card hand
        hand = random.sample(CARDS, 5)
        # Add the hand to the list of drawn cards
        drawn_cards.append(hand)
        # Increment the counter for each card in the hand
        for card in hand:
            counter[card] += 1

    # Return the list of drawn cards and the counter
    return drawn_cards, counter