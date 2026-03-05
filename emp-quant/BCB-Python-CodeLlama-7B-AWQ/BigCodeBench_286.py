from collections import Counter
import os
import csv
def task_func(output_file, test_directory):
    """
    Count the number of words in multiple dictionary files (.txt) in a specific directory, export the counts to a CSV file, and then return the total number of words.
    Note that:
    - Header for the csv output file is "Word", "Count"
    - Return 0 if the input invalid or error raised
    """
    # Check if the input directory is valid
    if not os.path.isdir(test_directory):
        print("Invalid input directory")
        return 0

    # Create a list to store the words and their counts
    word_counts = []

    # Loop through the files in the directory
    for filename in os.listdir(test_directory):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(test_directory, filename), 'r') as f:
                contents = f.read()

            # Tokenize the contents into individual words
            words = contents.split()

            # Create a Counter object to count the words
            counter = Counter(words)

            # Add the counts to the word_counts list
            for word, count in counter.items():
                word_counts.append((word, count))

    # Write the word counts to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        for word, count in word_counts:
            writer.writerow([word, count])

    # Return the total number of words
    return sum(count for word, count in word_counts)
test_directory = './yourdictfiles/'
output_file = './output.csv'