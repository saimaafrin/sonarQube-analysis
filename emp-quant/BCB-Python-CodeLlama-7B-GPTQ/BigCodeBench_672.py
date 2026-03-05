import csv
import sys
def task_func(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for line in reversed(lines):
            writer.writerow(line)
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
    assert lines == [line for line in reversed(lines)]
    return filename