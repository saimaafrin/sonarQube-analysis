import pandas as pd
import itertools
import random
def task_func(colors, states):
    # Generate all combinations of colors and states
    combinations = list(itertools.product(colors, states))
    
    # Shuffle the combinations
    random.shuffle(combinations)
    
    # Determine the number of columns based on the smaller list length
    num_columns = min(len(colors), len(states))
    
    # Create a DataFrame with the combinations distributed across columns
    df = pd.DataFrame(combinations, columns=[f'Color:State_{i+1}' for i in range(num_columns)])
    
    return df