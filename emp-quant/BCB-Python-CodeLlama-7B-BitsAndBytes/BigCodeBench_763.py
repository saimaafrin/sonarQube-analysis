
import numpy as np
from collections import defaultdict
import json
import csv

# Constants
INPUT_FILE = 'input.json'
OUTPUT_FILE = 'output.csv'

# Function to calculate mean and median of a list of numbers
def calculate_stats(numbers):
    mean = np.mean(numbers)
    median = np.median(numbers)
    return mean, median

# Function to read JSON data from file
def read_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

# Function to write CSV data to file
def write_csv(data, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value['mean'], value['median']])

# Main function
def task_func(input_file, output_file):
    data = read_json(input_file)
    results = defaultdict(dict)
    for d in data:
        for key, value in d.items():
            if isinstance(value, list):
                mean, median = calculate_stats(value)
                results[key]['mean'] = mean
                results[key]['median'] = median
    write_csv(results, output_file)

# Call the main function
task_func(INPUT_FILE, OUTPUT_FILE)