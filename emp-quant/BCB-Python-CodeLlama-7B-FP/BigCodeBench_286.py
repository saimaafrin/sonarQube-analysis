from collections import Counter
import os
import csv
def task_func(output_file, test_directory):
    """
    Count the number of words in multiple dictionary files (.txt) in a specific directory, export the counts to a CSV file, and then return the total number of words.
    Note that: Header for the csv output file is "Word", "Count"
    Return 0 if the input invalid or error raised
    """
    # Check if the input is valid
    if not os.path.isdir(test_directory):
        return 0

    # Initialize the counter
    counter = Counter()

    # Iterate over the files in the directory
    for filename in os.listdir(test_directory):
        # Check if the file is a .txt file
        if not filename.endswith('.txt'):
            continue

        # Open the file and read its contents
        with open(os.path.join(test_directory, filename), 'r') as f:
            contents = f.read()

        # Split the contents into words
        words = contents.split()

        # Update the counter
        counter.update(words)

    # Write the counter to a CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Word', 'Count'])
        for word, count in counter.items():
            writer.writerow([word, count])

    # Return the total number of words
    return sum(counter.values())
test_directory = './yourdictfiles/'
output_file = './output.csv'