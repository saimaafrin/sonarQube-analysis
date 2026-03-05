
import numpy as np
from collections import defaultdict
import json
import csv

# Constants
input_file = "data.json"
output_file = "results.csv"

# Load the data
with open(input_file, "r") as f:
    data = json.load(f)

# Create a dictionary to store the results
results = defaultdict(lambda: defaultdict(float))

# Calculate the mean and median for each key
for key in data:
    values = [int(x[key]) for x in data]
    results[key]["mean"] = np.mean(values)
    results[key]["median"] = np.median(values)

# Write the results to a CSV file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    for key in results:
        writer.writerow([key, results[key]["mean"], results[key]["median"]])