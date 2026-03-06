
import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    # Open the CSV file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)

        # Create a dictionary to store the counts
        counts = collections.defaultdict(int)

        # Iterate over the rows in the CSV file
        for row in reader:
            # Check if the employee ID starts with the specified prefix
            if row[0].startswith(emp_prefix):
                # Increment the count for the employee ID
                counts[row[0]] += 1

    # Return the dictionary with the counts
    return counts