import collections
import numpy as np
def task_func(file_name):
    # Check if the file is empty
    if not os.path.getsize(file_name):
        return {}
    
    # Read the CSV file
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the column names
        data = np.array(list(reader))  # Convert the rest of the data to a numpy array
    
    # Initialize a dictionary to store the most common values
    most_common_values = {}
    
    # Iterate over each column
    for i, header in enumerate(headers):
        column = data[:, i]
        # Count the occurrences of each value in the column
        value_counts = collections.Counter(column)
        # Find the most common value
        most_common = value_counts.most_common()
        # If there are multiple values with the same count, sort them alphabetically
        if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
            most_common.sort(key=lambda x: x[0])
        # Store the most common value in the dictionary
        most_common_values[header] = most_common[0][0]
    
    return most_common_values