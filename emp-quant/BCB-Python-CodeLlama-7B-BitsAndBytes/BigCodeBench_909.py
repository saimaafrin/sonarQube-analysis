
import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Shuffle the categories
    shuffle(categories)

    # Create a dictionary to map each letter to a category
    letter_to_category = {letter: categories[i] for i, letter in enumerate(letters)}

    # Create a list of tuples with the letter and category
    data = [(letter, letter_to_category[letter]) for letter in letters]

    # Create a Pandas DataFrame with the data
    df = pd.DataFrame(data, columns=['Letter', 'Category'])

    return df