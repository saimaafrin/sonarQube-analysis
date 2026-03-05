
import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Shuffle the categories
    shuffle(categories)
    # Create a dictionary with the letters as keys and the categories as values
    letter_category_dict = {letter: category for letter, category in zip(letters, categories)}
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(letter_category_dict, columns=['Letter', 'Category'])
    return df