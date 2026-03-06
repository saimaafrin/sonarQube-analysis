
import collections
import pandas as pd

def task_func(obj_list, attr):
    # Extract the values of the specified attribute from the list of objects
    attribute_values = [getattr(obj, attr) for obj in obj_list if hasattr(obj, attr)]
    
    # Count the frequency of each value using collections.Counter
    counter = collections.Counter(attribute_values)
    
    # Create a DataFrame from the Counter object
    df = pd.DataFrame(list(counter.items()), columns=['attribute', 'count'])
    
    return df