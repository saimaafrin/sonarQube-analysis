
import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Create a list of tuples with all possible combinations of letters and categories
    combined = list(itertools.product(letters, categories))
    # Shuffle the list of tuples
    shuffle(combined)
    # Create a DataFrame from the shuffled list of tuples
    df = pd.DataFrame(combined, columns=['Letter', 'Category'])
    return df