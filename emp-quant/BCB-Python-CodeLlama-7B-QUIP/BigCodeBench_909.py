
import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    shuffled_categories = shuffle(categories)
    shuffled_letters = shuffle(letters)
    return pd.DataFrame({
        'Letter': shuffled_letters,
        'Category': shuffled_categories
    })