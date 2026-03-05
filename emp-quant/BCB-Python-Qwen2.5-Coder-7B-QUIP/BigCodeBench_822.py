
import random
import string
# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    # Generate a list of random characters from letters and digits
    password_chars = [random.choice(LETTERS) for _ in range(length - num_digits)] + [random.choice(DIGITS) for _ in range(num_digits)]
    
    # Shuffle the list to ensure randomness
    random.shuffle(password_chars)
    
    # Convert the list to a string and return
    return ''.join(password_chars)