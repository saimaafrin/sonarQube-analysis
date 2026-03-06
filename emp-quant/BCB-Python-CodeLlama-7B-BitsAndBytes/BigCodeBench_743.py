
import json
import os

# Constants
PREFIXES = ["is_", "has_", "can_", "should_"]

def task_func(directory):
    # Create an empty dictionary to store the statistics
    statistics = {}

    # Iterate over all JSON files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            # Open the JSON file and load its content
            with open(os.path.join(directory, filename), "r") as f:
                data = json.load(f)

            # Iterate over all keys in the JSON data
            for key in data.keys():
                # Check if the key starts with any of the prefixes
                for prefix in PREFIXES:
                    if key.startswith(prefix):
                        # Increment the count for the prefix
                        if prefix not in statistics:
                            statistics[prefix] = 0
                        statistics[prefix] += 1

    # Return the statistics dictionary
    return statistics