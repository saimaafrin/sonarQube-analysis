import pandas as pd
import itertools
from random import shuffle
def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    """
    Create a Pandas DataFrame by associating each element from a list of letters to a category from a list of categories.
    The categories are randomly shuffled.
    """
    # Create a list of tuples with the letters and categories
    letters_categories = list(itertools.product(letters, categories))
    # Shuffle the list of tuples
    shuffle(letters_categories)
    # Create a Pandas DataFrame with the shuffled list of tuples
    df = pd.DataFrame(letters_categories, columns=['Letter', 'Category'])
    return df