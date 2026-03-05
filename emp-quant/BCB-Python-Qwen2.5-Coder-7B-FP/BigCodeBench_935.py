import pandas as pd
import string
def task_func(word):
    # Check if the word is in lowercase and contains only alphabetic characters
    if not word.islower() or not word.isalpha():
        raise ValueError("Input word must be in lowercase and contain only alphabetic characters.")
    
    # Create a list of tuples with each letter and its position in the alphabet
    data = [(letter, string.ascii_lowercase.index(letter) + 1) for letter in word]
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Letter', 'Position'])
    
    return df