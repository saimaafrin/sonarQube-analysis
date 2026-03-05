import pandas as pd
import re
def task_func(text):
    """
    Extract data from a text and create a Pandas DataFrame.
    The text contains several lines, each formatted as 'Score: 85, Category: Math'.
    Make sure to convert the scores in integer.
    """
    # Extract the scores and categories from the text
    scores = re.findall(r'Score: (\d+), Category: (\w+)', text)

    # Create a list of dictionaries with the extracted data
    data = [{'score': int(score), 'category': category} for score, category in scores]

    # Create a Pandas DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Return the DataFrame
    return df
text = """
Score: 85, Category: Math
Score: 70, Category: Science
Score: 90, Category: English
"""