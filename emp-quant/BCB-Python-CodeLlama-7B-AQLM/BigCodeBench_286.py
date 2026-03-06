from collections import Counter
import os
import csv
def task_func(output_file, test_directory):
    """
    Count the number of words in multiple dictionary files (.txt) in a specific directory,
    export the counts to a CSV file, and then return the total number of words.

    Parameters:
    filename (str): The name of the output CSV file.
    test_directory (str): The directory containing the dictionary files (.txt).

    Returns:
    int: total number of words in .txt files

    Note:
    - Header for the csv output file is "Word", "Count"
    - Return 0 if the input invalid or error raised

    Requirements:
    - collections.Counter
    - os
    - csv

    Example:
    >>> task_func('word_counts.csv')
    10
    """
    # TODO: Implement this function
    # Hint:
    # - Use os.listdir() to get a list of files in the directory
    # - Use Counter to count the number of words in each file
    # - Use csv.writer to write the counts to the output file
    # - Return the total number of words

    # Get the list of files in the directory
    file_list = os.listdir(test_directory)

    # Initialize the counter
    word_counter = Counter()

    # Loop through the files in the directory
    for file in file_list:
        # Open the file
        with open(test_directory + file, 'r') as f:
            # Read the file
            file_content = f.read()
            # Split the file content into a list of words
            file_content_list = file_content.split()
            # Update the counter
            word_counter.update(file_content_list)

    # Write the counts to the output file
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Word', 'Count'])
        for word, count in word_counter.items():
            writer.writerow([word, count])

    # Return the total number of words
    return sum(word_counter.values())