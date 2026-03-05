import random
import string
LETTERS = string.ascii_letters
DIGITS = string.digits
def task_func(length, num_digits):
    """
    Generates a random password with a specified length and number of digits.
    
    Parameters:
    length (int): The total length of the password.
    num_digits (int): The number of digits in the password.
    
    Returns:
    str: A string representing the randomly generated password.
    """
    if num_digits > length or num_digits < 0:
        raise ValueError("Number of digits must be between 0 and the length of the password.")
    
    # Generate a list of random letters and digits
    password_list = [random.choice(LETTERS) for _ in range(length - num_digits)] + [random.choice(DIGITS) for _ in range(num_digits)]
    
    # Shuffle the list to ensure randomness
    random.shuffle(password_list)
    
    # Convert the list to a string and return
    return ''.join(password_list)