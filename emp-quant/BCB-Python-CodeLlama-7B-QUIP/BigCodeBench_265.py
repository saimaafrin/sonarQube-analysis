
import collections
import json
import os

def task_func(data, json_file_name='data.json'):
    data['a'] = 1
    freq = collections.Counter(data.values())
    with open(json_file_name, 'w') as f:
        json.dump({'data': data, 'freq': freq}, f, indent=4)
    return json_file_name