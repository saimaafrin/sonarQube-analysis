from collections import Counter
import pandas as pd
def task_func(myList):
    """
    Count the frequency of each word in a list and return a DataFrame of words and their number.
    """
    # Create a Counter object from the list
    counter = Counter(myList)

    # Create a list of tuples with words and their counts
    word_counts = [(word, count) for word, count in counter.items()]

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(word_counts, columns=['word', 'count'])

    return df
myList = ['apple', 'banana', 'orange', 'banana', 'apple']