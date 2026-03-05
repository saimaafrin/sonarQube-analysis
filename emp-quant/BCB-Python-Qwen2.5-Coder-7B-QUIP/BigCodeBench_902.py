
import pandas as pd
from collections import Counter
def task_func(d):
    # Initialize Counter objects for each key
    counters = {'x': Counter(), 'y': Counter(), 'z': Counter()}
    
    # Iterate through the list of dictionaries
    for item in d:
        # Update the Counter for each key based on the values in the dictionary
        counters['x'].update(item['x'])
        counters['y'].update(item['y'])
        counters['z'].update(item['z'])
    
    # Return the dictionary of Counter objects
    return {'x': counters['x'], 'y': counters['y'], 'z': counters['z']}