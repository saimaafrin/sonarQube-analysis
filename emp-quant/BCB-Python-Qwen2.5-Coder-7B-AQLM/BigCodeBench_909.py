
import pandas as pd
import itertools
from random import shuffle

def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Shuffle the categories to ensure randomness
    shuffle(categories)
    
    # Create a list of tuples by pairing each letter with a category
    data = list(itertools.product(letters, categories))
    
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Letter', 'Category'])
    
    return df