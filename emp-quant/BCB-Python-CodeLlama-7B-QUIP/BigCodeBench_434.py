
import pandas as pd
import re
import random

def task_func(s: str, seed: int = 0) -> pd.DataFrame:
    # Remove trailing whitespaces
    s = re.sub(r'\s+$', '', s)

    # Split the input string into segments
    segments = s.split('\n')

    # Create a list to hold the data
    data = []

    # Loop through each segment
    for segment in segments:
        # Split the segment into parts
        parts = segment.split()

        # Remove any empty parts
        parts = [part for part in parts if part != '']

        # Add the data to the list
        data.append({
            'ID': parts[0],
            'Quantity': parts[1],
            'Code': parts[2],
            'Price': parts[3],
            'Product': random.choice(['Apple', 'Banana', 'Orange', 'Pear', 'Grape']),
            'Description': parts[4]
        })

    # Create the DataFrame
    data_df = pd.DataFrame(data)

    return data_df