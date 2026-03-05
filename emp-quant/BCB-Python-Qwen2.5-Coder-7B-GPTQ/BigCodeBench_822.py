import random
import string
LETTERS = string.ascii_letters
DIGITS = string.digits
def task_func(length, num_digits):
    """
    Generates a random password with a specified length and number of digits.
    
    :param length: Total length of the password
    :param num_digits: Number of digits in the password
    :return: A string representing the randomly generated password
    """
    if num_digits > length or num_digits < 0:
        raise ValueError("Number of digits must be between 0 and the length of the password")
    
    # Generate the required number of digits
    password_digits = ''.join(random.choice(DIGITS) for _ in range(num_digits))
    
    # Generate the remaining characters as letters
    remaining_length = length - num_digits
    password_letters = ''.join(random.choice(LETTERS) for _ in range(remaining_length))
    
    # Combine digits and letters
    password = password_digits + password_letters
    
    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    
    return final_password