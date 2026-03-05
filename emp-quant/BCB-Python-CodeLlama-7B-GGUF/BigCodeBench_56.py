
import pandas as pd
import re

def task_func(text):
    # Extract data from text
    data = re.findall(r'Score: (\d+), Category: (\w+)', text)

    # Create DataFrame
    df = pd.DataFrame(data, columns=['Score', 'Category'])

    # Convert scores to integer
    df['Score'] = df['Score'].astype(int)

    return df