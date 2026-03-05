import pandas as pd
import re
def task_func(text):
    """
    Extract data from a text and create a Pandas DataFrame.
    The text contains several lines, each formatted as 'Score: 85, Category: Math'.
    Make sure to convert the scores in integer.
    """
    # Extract the data from the text
    data = re.findall(r'Score: (\d+), Category: (\w+)', text)

    # Create a Pandas DataFrame with the extracted data
    df = pd.DataFrame(data, columns=['Score', 'Category'])

    # Convert the scores to integer
    df['Score'] = df['Score'].astype(int)

    return df
text = """
Score: 85, Category: Math
Score: 90, Category: Science
Score: 80, Category: English
Score: 75, Category: History
"""