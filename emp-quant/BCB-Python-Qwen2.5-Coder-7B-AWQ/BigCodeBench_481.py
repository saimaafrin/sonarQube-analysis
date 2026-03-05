import pandas as pd
import random
import re
def task_func(data_list, seed=42):
    """
    Randomizes the order of comma-separated substrings within each string in a list,
    normalizing spaces to ensure a single space follows each comma using regex, then
    returns a DataFrame comparing original and randomized strings.
    
    Parameters:
    - data_list: List of strings to be processed.
    - seed: Seed for random number generator for reproducibility.
    
    Returns:
    - pandas.DataFrame: A DataFrame with columns 'Original String' and 'Randomized String'.
    """
    # Set the seed for random number generator
    random.seed(seed)
    
    # Initialize lists to store original and randomized strings
    original_strings = []
    randomized_strings = []
    
    # Process each string in the input list
    for item in data_list:
        # Normalize spaces using regex
        normalized_item = re.sub(r'\s+', ' ', item)
        
        # Split the string by commas
        substrings = normalized_item.split(',')
        
        # Randomize the order of substrings
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string
        randomized_item = ', '.join(substrings)
        
        # Append the original and randomized strings to the respective lists
        original_strings.append(normalized_item)
        randomized_strings.append(randomized_item)
    
    # Create a DataFrame to compare original and randomized strings
    result_df = pd.DataFrame({
        'Original String': original_strings,
        'Randomized String': randomized_strings
    })
    
    return result_df
data_list = [
    "apple, banana, cherry",
    "dog, cat, bird, fish",
    "red, green, blue, yellow"
]