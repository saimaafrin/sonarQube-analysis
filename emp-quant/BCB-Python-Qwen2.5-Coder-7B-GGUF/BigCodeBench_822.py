
import random
import string

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    # Ensure the number of digits does not exceed the total length
    if num_digits > length:
        raise ValueError("Number of digits cannot exceed the total length of the password.")
    
    # Generate the password with the specified number of digits and letters
    password = [random.choice(DIGITS) for _ in range(num_digits)] + [random.choice(LETTERS) for _ in range(length - num_digits)]
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)