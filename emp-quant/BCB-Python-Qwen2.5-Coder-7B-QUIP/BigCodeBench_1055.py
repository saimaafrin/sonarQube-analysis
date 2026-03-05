
import pandas as pd
import itertools
import random

def task_func(colors, states):
    # Generate all combinations using Cartesian product
    combinations = list(itertools.product(colors, states))
    
    # Shuffle the combinations
    random.shuffle(combinations)
    
    # Determine the number of columns
    num_columns = min(len(colors), len(states))
    
    # Create a DataFrame with the shuffled combinations
    df = pd.DataFrame(combinations, columns=[f"Column{i}" for i in range(1, num_columns + 1)])
    
    # Format the DataFrame to display as "Color:State"
    df.columns = [f"Column{i}" for i in range(1, num_columns + 1)]
    df = df.applymap(lambda x: f"{x[0]}:{x[1]}")
    
    return df