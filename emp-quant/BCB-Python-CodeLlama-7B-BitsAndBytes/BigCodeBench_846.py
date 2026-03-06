
import collections
import pandas as pd

class ExampleObject:
    def __init__(self, animal, shape):
        self.animal = animal
        self.shape = shape

obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]

def task_func(obj_list, attr):
    counts = collections.Counter()
    for obj in obj_list:
        counts[getattr(obj, attr)] += 1
    return pd.DataFrame({'attribute': counts.keys(), 'count': counts.values()})

count = task_func(obj_list, 'shape')
print(count)