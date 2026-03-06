import pandas as pd
import regex as re
def task_func(text):
    """
    Extract data from a text and create a Pandas DataFrame. The text contains several lines, each formatted as 'Score: 85, Category: Math'. Make sure to convert the scores in integer.

    Parameters:
    text (str): The text to analyze.

    Returns:
    DataFrame: A pandas DataFrame with extracted data.

    Requirements:
    - pandas
    - regex

    Example:
    >>> text = "Score: 85, Category: Math\\nScore: 90, Category: Science\\nScore: 80, Category: Math"
    >>> df = task_func(text)
    >>> print(df)
       Score Category
    0     85     Math
    1     90  Science
    2     80     Math
    """
    # TODO: Implement the task
    # 1. Split the text into lines
    lines = text.split('\n')
    # 2. Create a list of tuples with the score and category
    data = [(int(re.search(r'Score: (\d+)', line).group(1)), re.search(r'Category: (.*)', line).group(1)) for line in lines]
    # 3. Create a DataFrame with the data
    df = pd.DataFrame(data, columns=['Score', 'Category'])
    return df