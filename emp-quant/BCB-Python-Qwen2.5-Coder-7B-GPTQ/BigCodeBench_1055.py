import pandas as pd
import itertools
import random
def task_func(colors, states):
    # Generate all possible combinations of colors and states
    combinations = list(itertools.product(colors, states))
    
    # Shuffle the combinations to ensure randomness
    random.shuffle(combinations)
    
    # Determine the number of columns based on the smaller list length
    num_columns = min(len(colors), len(states))
    
    # Create a DataFrame with the shuffled combinations
    df = pd.DataFrame(combinations[:num_columns * len(combinations) // num_columns], columns=[f"Column_{i+1}" for i in range(num_columns)])
    
    # Format each cell to "Color:State"
    df = df.applymap(lambda x: f"{x[0]}:{x[1]}")
    
    return df