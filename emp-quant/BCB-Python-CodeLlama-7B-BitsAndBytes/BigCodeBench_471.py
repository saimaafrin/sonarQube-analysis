
from collections import Counter
import pandas as pd

def task_func(myList):
    # Create a Counter object from the list
    counter = Counter(myList)

    # Convert the Counter object to a DataFrame
    df = pd.DataFrame(counter.items(), columns=['word', 'count'])

    # Sort the DataFrame by count in descending order
    df.sort_values(by='count', ascending=False, inplace=True)

    return df