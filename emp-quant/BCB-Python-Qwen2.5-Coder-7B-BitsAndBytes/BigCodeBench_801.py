
import collections
import numpy as np

def task_func(file_name):
    if not file_name or not os.path.exists(file_name):
        return {}

    result = {}
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = {key: [] for key in reader.fieldnames}

        for row in reader:
            for key, value in row.items():
                data[key].append(value)

    for key, values in data.items():
        counter = collections.Counter(values)
        most_common_values = counter.most_common()
        if most_common_values:
            most_common_value = most_common_values[0][0]
            # Handle ties by sorting alphabetically
            while most_common_values and most_common_values[0][1] == most_common_values[1][1]:
                most_common_values.sort(key=lambda x: x[0])
                most_common_value = most_common_values[0][0]
            result[key] = most_common_value

    return result