
import pandas as pd
import re
import random

def task_func(s: str, seed: int = 0) -> pd.DataFrame:
    # Split the input string into segments by newlines
    segments = s.strip().split('\n')
    
    # Initialize a list to store the data rows
    data = []
    
    # Initialize a dictionary to store product names by code
    product_names = {}
    
    # Initialize a list of possible product names
    possible_names = ['Apple', 'Banana', 'Orange', 'Pear', 'Grape']
    
    # Initialize a random seed for reproducibility
    random.seed(seed)
    
    # Iterate over the segments
    for segment in segments:
        # Split the segment into parts
        parts = segment.split()
        
        # Assign a product name to the current code if it doesn't exist
        if parts[2] not in product_names:
            product_names[parts[2]] = random.choice(possible_names)
        
        # Append the data row to the list
        data.append({
            'ID': int(parts[0]),
            'Quantity': int(parts[1]),
            'Code': parts[2],
            'Price': int(parts[3]),
            'Product': product_names[parts[2]],
            'Description': ' '.join(parts[4:])
        })
    
    # Create the DataFrame from the data
    data_df = pd.DataFrame(data)
    
    return data_df