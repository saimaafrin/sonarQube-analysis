
import pandas as pd
from collections import Counter

def task_func(d):
    result = {'x': Counter(), 'y': Counter(), 'z': Counter()}
    for item in d:
        if 'x' in item:
            result['x'].update(item['x'])
        if 'y' in item:
            result['y'].update(item['y'])
        if 'z' in item:
            result['z'].update(item['z'])
    return result