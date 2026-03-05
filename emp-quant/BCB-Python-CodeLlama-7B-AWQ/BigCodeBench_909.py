import pandas as pd
import itertools
from random import shuffle
def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    """
    Create a Pandas DataFrame by associating each element from a list of letters to a category from a list of categories.
    The categories are randomly shuffled.
    """
    # Create a list of tuples with each letter and its corresponding category
    letter_category_list = [(letter, categories[i]) for i, letter in enumerate(letters)]

    # Shuffle the categories
    shuffle(categories)

    # Create a DataFrame with the letter and category columns
    df = pd.DataFrame(letter_category_list, columns=['Letter', 'Category'])

    return df
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
categories = ['Category 1', 'Category 2', 'Category 3']