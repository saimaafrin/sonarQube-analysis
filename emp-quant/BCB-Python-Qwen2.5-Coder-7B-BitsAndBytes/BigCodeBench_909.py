
import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Create a dictionary to hold the mapping of letters to categories
    letter_to_category = dict(itertools.zip_longest(letters, categories * (len(letters) // len(categories) + 1)))
    
    # Shuffle the categories
    shuffle(categories)
    
    # Create a new dictionary to hold the shuffled mapping
    shuffled_letter_to_category = {letter: categories[i % len(categories)] for i, letter in enumerate(letters)}
    
    # Create a DataFrame from the shuffled mapping
    df = pd.DataFrame(list(shuffled_letter_to_category.items()), columns=['Letter', 'Category'])
    
    return df