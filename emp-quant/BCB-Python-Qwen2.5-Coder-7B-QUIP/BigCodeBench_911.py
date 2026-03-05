
from functools import reduce
import operator
import string

def task_func(letters):
    # Create a dictionary to map uppercase letters to their corresponding numbers
    letter_to_number = {letter: idx + 1 for idx, letter in enumerate(string.ascii_uppercase)}
    
    # Convert the list of letters to a list of numbers using the dictionary
    numbers = [letter_to_number[letter] for letter in letters]
    
    # Calculate the product of the numbers
    product = reduce(operator.mul, numbers, 1)
    
    return product