import collections
import numpy as np
def task_func(file_name):
    # Check if the file is empty
    if not os.path.getsize(file_name):
        return {}
    
    # Initialize a dictionary to store the most common values
    most_common_values = {}
    
    # Read the CSV file
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the column headers
        
        # Initialize a list of lists to store the values of each column
        columns = [[] for _ in headers]
        
        # Read the values of each column
        for row in reader:
            for i, value in enumerate(row):
                columns[i].append(value)
    
    # Find the most common value in each column
    for i, column in enumerate(columns):
        # Count the occurrences of each value in the column
        value_counts = collections.Counter(column)
        
        # Find the most common value
        if value_counts:
            most_common_value = value_counts.most_common(1)[0][0]
            # If there are multiple values with the same count, sort them alphabetically
            if len(value_counts) > 1:
                most_common_values[headers[i]] = sorted(value_counts.keys())[0]
            else:
                most_common_values[headers[i]] = most_common_value
        else:
            most_common_values[headers[i]] = None
    
    return most_common_values