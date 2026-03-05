import random
import string
LETTERS = string.ascii_letters
DIGITS = string.digits
def task_func(length, num_digits):
    """
    Generate a random password with a specified length and number of digits.
    The function creates a random password consisting of letters and digits.
    The total length of the password and the number of digits in it are specified by the user.
    The characters in the password are randomly shuffled to ensure variability.
    """
    # Generate a random password consisting of letters and digits
    password = ''.join(random.choice(LETTERS + DIGITS) for _ in range(length))
    # Shuffle the characters in the password to ensure variability
    random.shuffle(password)
    # Return the generated password
    return password