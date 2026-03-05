from collections import Counter
import pandas as pd
def task_func(myList):
    """
    Count the frequency of each word in a list and return a DataFrame of words and their number.
    """
    counter = Counter(myList)
    df = pd.DataFrame(counter.items(), columns=['word', 'count'])
    return df
myList = ['apple', 'banana', 'orange', 'apple', 'banana', 'orange']