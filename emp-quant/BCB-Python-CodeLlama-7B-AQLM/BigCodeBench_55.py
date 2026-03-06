import re
import pandas as pd
def task_func(text):
    """
    Given a text as input, the function should split it into multiple sentences and build a dictionary where each key is associated with a sentence and the corresponding value is the number of words in the sentence. The function returns a pandas Series built from the dictionary.
    - The keys of the dictionary (which correspond to the Index of the pandas Series) should be named "Sentence 1", "Sentence 2" etc.
    - When counting the words in a sentence, do not consider those included in the constant STOPWORDS.
    - Do not consider empty sentences.

    Parameters:
    text (str): The text to analyze.

    Returns:
    pandas.core.series.Series: A pandas Series each sentence and its number of words that are not in STOPWORDS.

    Requirements:
    - pandas
    - regex

    Example:
    >>> text = "This is a sample sentence. This sentence contains sample words."
    >>> df = task_func("I am good at programming. I learned it in college.")
    >>> print(df)
    Sentence 1    5
    Sentence 2    5
    dtype: int64
    """
    # TODO: Implement the function
    # Hint: Use the regex library to split the text into sentences
    # Hint: Use the pandas Series constructor to build the Series
    # Hint: Use the len() function to count the number of words in a sentence
    # Hint: Use the filter() function to remove the stopwords
    # Hint: Use the zip() function to create a dictionary
    # Hint: Use the pandas Series constructor to build the Series
    # Hint: Use the map() function to convert the values of the Series to int
    # Hint: Use the sort_index() function to sort the index of the Series
    # Hint: Use the rename() function to rename the index of the Series
    # Hint: Use the dropna() function to remove empty sentences
    # Hint: Use the reset_index() function to reset the index of the Series
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the Series
    # Hint: Use the rename() function to rename the index of the Series
    # Hint: Use the to_frame() function to convert the Series to a DataFrame
    # Hint: Use the reset_index() function to reset the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the drop() function to remove the "index" column
    # Hint: Use the sort_index() function to sort the index of the DataFrame
    # Hint: Use the rename() function to rename the index of the DataFrame
    # Hint: Use the to_csv() function to save the DataFrame to a CSV file
    # Hint: Use the read_csv() function to read the CSV file and return a DataFrame
    # Hint: Use the sort_index() function to sort the index of the DataFrame