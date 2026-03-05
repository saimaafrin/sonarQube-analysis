import collections
import numpy as np
def task_func(file_name):
    # Check if the file is empty
    if not os.path.getsize(file_name):
        return {}
    
    # Read the CSV file
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get the column names
        data = np.array(list(reader))  # Convert the rest of the data to a numpy array
    
    # Initialize a dictionary to store the most common values
    most_common_values = {}
    
    # Iterate over each column
    for i, column_name in enumerate(header):
        # Get the column data
        column_data = data[:, i]
        
        # Count the occurrences of each value
        value_counts = collections.Counter(column_data)
        
        # Find the most common value
        if value_counts:
            most_common_value = value_counts.most_common(1)[0][0]
            # If there are ties, sort them alphabetically and take the first
            if len(value_counts) > 1 and value_counts.most_common(2)[0][1] == value_counts.most_common(2)[1][1]:
                tied_values = [value for value, count in value_counts.most_common() if count == value_counts.most_common(1)[0][1]]
                tied_values.sort()
                most_common_value = tied_values[0]
        else:
            most_common_value = None
        
        # Store the most common value in the dictionary
        most_common_values[column_name] = most_common_value
    
    return most_common_values