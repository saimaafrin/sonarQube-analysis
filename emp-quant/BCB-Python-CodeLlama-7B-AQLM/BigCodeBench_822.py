import random
import string
LETTERS = string.ascii_letters
DIGITS = string.digits
def task_func(length, num_digits):
    """
    Generate a random password with a specified length and number of digits.

    The function creates a random password consisting of letters and digits. The total length of the password
    and the number of digits in it are specified by the user. The characters in the password are randomly
    shuffled to ensure variability.

    Parameters:
    - length (int): The total length of the password. Must be a positive integer.
    - num_digits (int): The number of digits to be included in the password. Must be a non-negative integer and
                      less than or equal to the total length of the password.

    Returns:
    - str: A string representing the randomly generated password.

    Requirements:
    - random
    - string

    Examples:
    >>> task_func(10, 3)
    'Vpbr812Ooh'
    >>> task_func(5, 2)
    '4Ob3h'
    """
    # Check that the length is a positive integer
    if not isinstance(length, int) or length <= 0:
        raise ValueError('The length must be a positive integer.')

    # Check that the number of digits is a non-negative integer and less than or equal to the length
    if not isinstance(num_digits, int) or num_digits < 0 or num_digits > length:
        raise ValueError('The number of digits must be a non-negative integer and less than or equal to the length.')

    # Create a list of letters and digits
    letters = list(LETTERS)
    digits = list(DIGITS)

    # Shuffle the letters and digits
    random.shuffle(letters)
    random.shuffle(digits)

    # Create a list of the specified length containing letters and digits
    password = []
    for i in range(length):
        if i < num_digits:
            password.append(random.choice(digits))
        else:
            password.append(random.choice(letters))

    # Shuffle the password
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)