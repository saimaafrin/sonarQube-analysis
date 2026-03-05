from collections import Counter
import os
import json
def task_func(filename, directory):
    """
    Count the number of words in .txt files within a specified directory, export the counts to a JSON file, and then return the total number of words.
    """
    # Create a list to store the counts of words in each file
    file_counts = []

    # Iterate over the files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a .txt file
            if file.endswith('.txt'):
                # Open the file and read its contents
                with open(os.path.join(root, file), 'r') as f:
                    contents = f.read()

                # Split the contents into individual words
                words = contents.split()

                # Create a Counter object to count the number of words
                counter = Counter(words)

                # Add the count to the list of file counts
                file_counts.append(counter)

    # Create a dictionary to store the counts of words in each file
    file_counts_dict = {}

    # Iterate over the files and add their counts to the dictionary
    for i, file_count in enumerate(file_counts):
        file_counts_dict[f'file_{i}'] = file_count

    # Export the counts to a JSON file
    with open(filename, 'w') as f:
        json.dump(file_counts_dict, f)

    # Return the total number of words
    return sum(file_counts)
filename = 'file_counts.json'
directory = '.'