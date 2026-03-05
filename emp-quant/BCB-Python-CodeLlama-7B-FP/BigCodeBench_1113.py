import csv
import collections
def task_func(csv_file, emp_prefix='EMP$$'):
    """
    Count the number of records for each employee in a CSV file.

    Args:
        csv_file (str): Path to the CSV file.
        emp_prefix (str, optional): Prefix for employee records. Defaults to 'EMP$$'.

    Returns:
        dict: A dictionary with the count of records for each employee.
    """
    # Open the CSV file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)

        # Create a dictionary to store the counts
        emp_counts = collections.defaultdict(int)

        # Iterate over the records in the CSV file
        for row in reader:
            # Check if the record is an employee record
            if row[0].startswith(emp_prefix):
                # Increment the count for the employee
                emp_counts[row[0]] += 1

        # Return the dictionary of counts
        return emp_counts