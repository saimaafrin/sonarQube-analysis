
import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    # Initialize a counter to keep track of employee record counts
    employee_counts = collections.Counter()
    
    # Open the CSV file and read its contents
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        
        # Skip the header row if present
        next(reader, None)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Check if the first column starts with the employee prefix
            if row[0].startswith(emp_prefix):
                # Extract the employee ID from the first column
                employee_id = row[0]
                # Increment the count for this employee ID
                employee_counts[employee_id] += 1
    
    # Return the dictionary containing employee counts
    return dict(employee_counts)