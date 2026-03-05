
import collections
import pandas as pd

def task_func(obj_list, attr):
    # Check if the attribute list is empty
    if not obj_list:
        return pd.DataFrame(columns=['attribute', 'count'])
    
    # Extract the attribute values from the list of objects
    attribute_values = [getattr(obj, attr) for obj in obj_list]
    
    # Count the frequency of each attribute value
    attribute_counts = collections.Counter(attribute_values)
    
    # Create a DataFrame from the counts
    count_df = pd.DataFrame(list(attribute_counts.items()), columns=['attribute', 'count'])
    
    return count_df

obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]
count = task_func(obj_list, 'shape')
print(count)