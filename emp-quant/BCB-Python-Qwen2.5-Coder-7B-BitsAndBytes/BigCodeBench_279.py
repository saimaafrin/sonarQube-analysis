
import random
from collections import Counter

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def task_func(x=1):
    """
    Draws x random 5-card poker hands from a 52-card pack (without suits).
    
    Parameters:
    x (int): Number of hands to draw. Default is 1.
    
    Returns:
    tuple: A tuple containing two elements:
        - list of list str: Each inner list contains 5 strings, representing a 5-card poker hand.
        - Counter: A counter of the drawn cards.
    """
    # Create a deck of cards
    deck = CARDS * 4
    
    # Shuffle the deck
    random.shuffle(deck)
    
    # Draw x hands
    hands = [deck[i:i+5] for i in range(0, len(deck), 5)[:x]]
    
    # Flatten the list of lists into a single list of cards
    all_cards = [card for hand in hands for card in hand]
    
    # Count the occurrences of each card
    card_counter = Counter(all_cards)
    
    return hands, card_counter