
import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    """
    Count the number of records for each employee in a CSV file.

    Args:
        csv_file (str): Path to the CSV file.
        emp_prefix (str, optional): Prefix for employee IDs. Defaults to 'EMP$$'.

    Returns:
        dict: A dictionary with the count of records for each employee.
    """
    employee_counts = collections.defaultdict(int)
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].startswith(emp_prefix):
                employee_counts[row[0]] += 1
    return employee_counts