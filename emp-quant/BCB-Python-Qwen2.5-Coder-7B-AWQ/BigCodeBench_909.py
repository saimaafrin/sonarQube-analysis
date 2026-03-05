import pandas as pd
import itertools
from random import shuffle
def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    # Create a list of all possible combinations of letters and categories
    combinations = list(itertools.product(letters, categories))
    
    # Shuffle the combinations to randomize the association
    shuffle(combinations)
    
    # Create a DataFrame from the shuffled combinations
    df = pd.DataFrame(combinations, columns=['Letter', 'Category'])
    
    return df