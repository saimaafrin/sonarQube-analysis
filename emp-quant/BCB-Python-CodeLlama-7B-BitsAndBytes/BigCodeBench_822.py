
import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    # Generate a random password with the specified length and number of digits
    password = ''.join(random.choice(LETTERS + DIGITS) for _ in range(length))
    # Shuffle the characters in the password to ensure variability
    random.shuffle(password)
    return password