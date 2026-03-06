
import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    if num_digits > length or num_digits < 0:
        raise ValueError("Number of digits must be between 0 and the length of the password.")
    
    # Generate the required number of digits
    password_digits = ''.join(random.choice(DIGITS) for _ in range(num_digits))
    
    # Generate the remaining characters as letters
    remaining_length = length - num_digits
    password_letters = ''.join(random.choice(LETTERS) for _ in range(remaining_length))
    
    # Combine digits and letters
    password_parts = list(password_digits + password_letters)
    
    # Shuffle the password parts to ensure randomness
    random.shuffle(password_parts)
    
    # Join the shuffled parts into a single string
    final_password = ''.join(password_parts)
    
    return final_password