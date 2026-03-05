
import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    """
    Generate a random password with the specified length and number of digits.

    Args:
        length (int): The total length of the password.
        num_digits (int): The number of digits in the password.

    Returns:
        str: A string representing the randomly generated password.
    """
    # Generate a list of random letters and digits
    letters_digits = random.sample(LETTERS + DIGITS, length)

    # Shuffle the list to ensure variability
    random.shuffle(letters_digits)

    # Return the password as a string
    return ''.join(letters_digits)