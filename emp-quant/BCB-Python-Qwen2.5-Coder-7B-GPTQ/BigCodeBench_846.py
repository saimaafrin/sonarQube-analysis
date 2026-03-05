import collections
import pandas as pd
def task_func(obj_list, attr):
    # Extract the attribute values from the list of objects
    attribute_values = [getattr(obj, attr) for obj in obj_list]
    
    # Count the frequency of each attribute value
    attribute_count = collections.Counter(attribute_values)
    
    # Create a DataFrame from the counter
    df = pd.DataFrame(list(attribute_count.items()), columns=['attribute', 'count'])
    
    return df
class ExampleObject:
    def __init__(self, animal, shape):
        self.animal = animal
        self.shape = shape
obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]