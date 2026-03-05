
import random
from collections import Counter
# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def task_func(x=1):
    def draw_hand(x):
        hand = []
        for i in range(x):
            hand.append(random.choice(CARDS))
        return hand
    def draw_hands(x):
        hands = []
        for i in range(x):
            hands.append(draw_hand(x))
        return hands
    def count_cards(hands):
        counter = Counter()
        for hand in hands:
            for card in hand:
                counter[card] += 1
        return counter
    hands = draw_hands(x)
    counter = count_cards(hands)
    return hands, counter