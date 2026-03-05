import csv
import collections
def task_func(csv_file, emp_prefix='EMP$$'):
    employee_record_count = collections.defaultdict(int)
    
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_id = row.get('employee_id')
            if employee_id and employee_id.startswith(emp_prefix):
                employee_record_count[employee_id] += 1
    
    return dict(employee_record_count)