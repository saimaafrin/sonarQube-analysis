
import csv
import sys

def task_func(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    lines = lines[::-1]
    
    with open(filename, 'w') as file:
        file.writelines(lines)
    
    return filename