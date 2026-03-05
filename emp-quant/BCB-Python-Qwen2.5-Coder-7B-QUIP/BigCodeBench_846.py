
import collections
import pandas as pd

def task_func(obj_list, attr):
    # Initialize a Counter to collect the frequency of each attribute value
    counter = collections.Counter()
    
    # Iterate through the list of objects and count the occurrences of each attribute value
    for obj in obj_list:
        # Assuming the attribute is a direct attribute of the object
        # and it's a string or can be converted to a string
        value = getattr(obj, attr, None)
        if value is not None:
            counter[value] += 1
    
    # Convert the Counter to a DataFrame
    df = pd.DataFrame(list(counter.items()), columns=['attribute', 'count'])
    
    # Return the DataFrame
    return df

obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]
count = task_func(obj_list, 'shape')
print(count)