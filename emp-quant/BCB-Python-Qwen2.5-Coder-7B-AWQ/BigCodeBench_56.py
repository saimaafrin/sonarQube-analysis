import pandas as pd
import regex as re
def task_func(text):
    # Define the regular expression pattern to extract scores and categories
    pattern = r'Score: (\d+), Category: (\w+)'
    
    # Use regex to find all matches in the text
    matches = re.findall(pattern, text)
    
    # Create a list of dictionaries to store the extracted data
    data = [{'Score': int(score), 'Category': category} for score, category in matches]
    
    # Create a pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    return df