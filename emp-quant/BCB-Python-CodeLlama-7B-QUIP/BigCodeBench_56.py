
import pandas as pd
import re

def task_func(text):
    # Create a regular expression to extract the scores and categories
    pattern = r"Score: (\d+), Category: (.+)"
    matches = re.findall(pattern, text)

    # Create a list of tuples with the scores and categories
    scores_and_categories = [(int(match[0]), match[1]) for match in matches]

    # Create a DataFrame with the extracted data
    df = pd.DataFrame(scores_and_categories, columns=["score", "category"])

    return df