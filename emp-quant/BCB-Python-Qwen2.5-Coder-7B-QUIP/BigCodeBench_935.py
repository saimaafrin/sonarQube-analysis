
import pandas as pd
import string

def task_func(word):
    # Check if the input word is in lowercase and contains only alphabetic characters
    if not word.islower() or not word.isalpha():
        raise ValueError("Input word must be in lowercase and contain only alphabetic characters.")
    
    # Create a list of dictionaries with letter and its position in the alphabet
    letter_positions = [{'Letter': letter, 'Position': (i + 1) % 26 + 1} for i, letter in enumerate(word)]
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(letter_positions)
    
    return df