import random
from collections import Counter
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    """
    Draw x random 5-card poker hands from a 52-card pack (without suits) and return the hands along with a counter of the drawn cards.
    The output is random; hence, the returned list will vary with each call.
    """
    # Initialize a list to store the drawn hands
    hands = []
    # Initialize a counter to keep track of the drawn cards
    counter = Counter()
    # Draw x hands
    for _ in range(x):
        # Initialize a list to store the cards in the hand
        hand = []
        # Draw 5 cards
        for _ in range(5):
            # Draw a random card from the deck
            card = random.choice(CARDS)
            # Add the card to the hand
            hand.append(card)
            # Increment the counter
            counter[card] += 1
        # Add the hand to the list of hands
        hands.append(hand)
    # Return the hands and the counter
    return hands, counter