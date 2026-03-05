
from collections import Counter
import pandas as pd

def task_func(myList):
    # Count the frequency of each word in the list
    word_counts = Counter(myList)
    
    # Create a DataFrame from the word counts
    df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    
    return df