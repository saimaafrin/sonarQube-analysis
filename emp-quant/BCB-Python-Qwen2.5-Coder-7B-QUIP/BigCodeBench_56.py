
import pandas as pd
import regex as re

def task_func(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize an empty list to store the data
    data = []
    
    # Regular expression to extract the score and category
    pattern = re.compile(r'Score: (\d+), Category: (.+)')
    
    # Iterate over the lines and extract the data
    for line in lines:
        match = pattern.match(line)
        if match:
            score = int(match.group(1))
            category = match.group(2)
            data.append((score, category))
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['Score', 'Category'])
    
    # Return the DataFrame
    return df