import pandas as pd
import itertools
import random
def task_func(colors, states):
    """
    Generates a pandas DataFrame containing shuffled combinations of provided colors and states.
    
    Parameters:
    colors (list): A list of color names.
    states (list): A list of state names.
    
    Returns:
    df (pandas.DataFrame): A DataFrame where each cell contains a string of the format "Color:State".
    """
    # Generate all combinations of colors and states
    combinations = list(itertools.product(colors, states))
    
    # Shuffle the combinations
    random.shuffle(combinations)
    
    # Determine the number of columns based on the smaller list length
    num_columns = min(len(colors), len(states))
    
    # Create a DataFrame with the shuffled combinations
    df = pd.DataFrame(combinations[:num_columns * len(combinations) // num_columns], columns=[f"Column{i+1}" for i in range(num_columns)])
    
    return df
colors = ["Red", "Green", "Blue"]
states = ["NY", "CA", "TX", "FL"]