import random
from collections import Counter
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    """
    Draws x random 5-card poker hands from a 52-card pack (without suits) and returns the hands along with a counter of the drawn cards.
    
    Parameters:
    x (int): The number of 5-card hands to draw. Default is 1.
    
    Returns:
    tuple: A tuple containing two elements:
        list of list str: Each inner list contains 5 strings, representing a 5-card poker hand.
        Counter: A counter of the drawn cards.
    """
    # Initialize an empty list to store the hands
    hands = []
    # Initialize a counter for the drawn cards
    card_counter = Counter()
    
    # Draw x hands
    for _ in range(x):
        # Shuffle the deck of cards
        random.shuffle(CARDS)
        # Draw 5 cards
        hand = CARDS[:5]
        # Add the hand to the list of hands
        hands.append(hand)
        # Update the counter with the drawn cards
        card_counter.update(hand)
    
    return hands, card_counter