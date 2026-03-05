
import csv
import collections

def task_func(csv_file, emp_prefix='EMP$$'):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        emp_counts = collections.Counter()
        for row in reader:
            if row[0].startswith(emp_prefix):
                emp_counts[row[0]] += 1
    return emp_counts