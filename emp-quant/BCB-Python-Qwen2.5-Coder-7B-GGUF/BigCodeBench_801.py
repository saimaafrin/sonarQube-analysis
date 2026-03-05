
import collections
import numpy as np

def task_func(file_name):
    if not file_name:
        return {}
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        return {}
    
    headers = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]
    
    if not data:
        return {}
    
    column_data = {header: [] for header in headers}
    
    for row in data:
        for header, value in zip(headers, row):
            column_data[header].append(value)
    
    most_common_values = {}
    
    for header, values in column_data.items():
        counter = collections.Counter(values)
        most_common = counter.most_common()
        if most_common:
            most_common_values[header] = sorted([value for value, count in most_common if count == most_common[0][1]])[0]
        else:
            most_common_values[header] = None
    
    return most_common_values