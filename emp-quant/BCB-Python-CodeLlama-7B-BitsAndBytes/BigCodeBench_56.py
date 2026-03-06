
import pandas as pd
import re

def task_func(text):
    # Extract the scores and categories from the text
    scores = re.findall(r'Score: (\d+), Category: (\w+)', text)

    # Create a list of dictionaries with the extracted data
    data = [{'score': int(score), 'category': category} for score, category in scores]

    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Return the DataFrame
    return df