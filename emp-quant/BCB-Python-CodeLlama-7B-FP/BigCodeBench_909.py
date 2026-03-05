import pandas as pd
import itertools
from random import shuffle
def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    """
    Create a Pandas DataFrame by associating each element from a list of letters to a category from a list of categories.
    The categories are randomly shuffled.
    """
    # Shuffle the categories
    shuffle(categories)

    # Create a dictionary to map each letter to a category
    letter_to_category = {letter: category for letter, category in zip(letters, categories)}

    # Create a list of tuples with the letter and category
    data = [(letter, category) for letter, category in letter_to_category.items()]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=['Letter', 'Category'])

    return df
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
categories = ['Category 1', 'Category 2', 'Category 3']