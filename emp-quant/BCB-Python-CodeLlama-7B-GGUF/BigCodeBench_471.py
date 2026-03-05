
from collections import Counter
import pandas as pd

def task_func(myList):
    counter = Counter(myList)
    df = pd.DataFrame(counter.items(), columns=['word', 'count'])
    return df