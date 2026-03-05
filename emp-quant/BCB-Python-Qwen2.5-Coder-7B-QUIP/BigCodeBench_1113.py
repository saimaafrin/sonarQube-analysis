
import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    # Initialize a dictionary to store the count of records for each employee
    employee_count = collections.defaultdict(int)

    # Open the CSV file and read the data
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Extract the employee ID from the row
            emp_id = row[0]
            # Check if the employee ID starts with the specified prefix
            if emp_id.startswith(emp_prefix):
                # Increment the count for the employee
                employee_count[emp_id] += 1

    # Return the dictionary with the count of records for each employee
    return dict(employee_count)