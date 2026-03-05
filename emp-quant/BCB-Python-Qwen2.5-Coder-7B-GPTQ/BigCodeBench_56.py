import pandas as pd
import regex as re
def task_func(text):
    # Use regex to find all occurrences of the pattern
    pattern = r'Score: (\d+), Category: (\w+)'
    matches = re.findall(pattern, text)
    
    # Create a list of dictionaries to store the data
    data = [{'Score': int(score), 'Category': category} for score, category in matches]
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    return df