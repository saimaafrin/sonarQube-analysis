
import pandas as pd
import regex as re

def task_func(text):
    # Define the pattern to extract score and category
    pattern = r'Score: (\d+), Category: (.+)'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Create a list of dictionaries for each match
    data = [{'Score': int(score), 'Category': category} for score, category in matches]
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    return df