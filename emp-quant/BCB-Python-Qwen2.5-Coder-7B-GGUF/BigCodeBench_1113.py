
import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    employee_counts = collections.defaultdict(int)
    
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_id = row.get('EmployeeID')
            if employee_id and employee_id.startswith(emp_prefix):
                employee_counts[employee_id] += 1
    
    return dict(employee_counts)