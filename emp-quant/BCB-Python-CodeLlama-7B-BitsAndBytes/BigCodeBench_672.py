
import csv
import sys

def task_func(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        lines.reverse()
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for line in lines:
                writer.writerow(line)
    f.seek(0)
    print(f"Inverted {filename}")