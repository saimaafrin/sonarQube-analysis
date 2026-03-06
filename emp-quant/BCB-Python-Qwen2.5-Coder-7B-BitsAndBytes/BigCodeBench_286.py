
from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    # Check if the test_directory exists
    if not os.path.exists(test_directory):
        print("Invalid directory")
        return 0
    
    word_counts = Counter()
    
    # Iterate through all files in the directory
    for filename in os.listdir(test_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(test_directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  # Convert to lowercase to count words case-insensitively
                    words = content.split()
                    word_counts.update(words)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    # Write the word counts to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Word", "Count"])
        for word, count in word_counts.items():
            writer.writerow([word, count])
    
    # Calculate the total number of words
    total_words = sum(word_counts.values())
    
    return total_words