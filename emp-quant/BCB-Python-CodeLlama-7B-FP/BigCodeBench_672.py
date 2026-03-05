import csv
import sys
def task_func(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        lines.reverse()
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(lines)