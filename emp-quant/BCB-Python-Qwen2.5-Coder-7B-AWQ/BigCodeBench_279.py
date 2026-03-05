import random
from collections import Counter
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    # Initialize an empty list to store the hands
    hands = []
    # Initialize a counter to keep track of the drawn cards
    card_counter = Counter()
    
    # Draw x random 5-card poker hands
    for _ in range(x):
        # Randomly select 5 cards from the CARDS list
        hand = random.sample(CARDS, 5)
        # Add the hand to the list of hands
        hands.append(hand)
        # Update the counter with the cards in the hand
        card_counter.update(hand)
    
    # Return the tuple containing the list of hands and the card counter
    return (hands, card_counter)