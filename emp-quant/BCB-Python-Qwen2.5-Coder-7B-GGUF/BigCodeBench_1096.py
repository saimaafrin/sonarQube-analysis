
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os
PUNCTUATION = set(punctuation)
def task_func(text, filename):
    # Tokenize the text using a regular expression that matches words
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    words = tokenizer.tokenize(text)
    
    # Filter out words that start with '$' and are not solely composed of punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in PUNCTUATION for char in word)]
    
    # Get the absolute path of the current working directory
    current_directory = os.getcwd()
    
    # Construct the full path for the CSV file
    csv_file_path = os.path.join(current_directory, filename)
    
    # Write the filtered words to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word'])  # Write the header
        writer.writerows([[word] for word in filtered_words])  # Write the words
    
    # Return the absolute path of the saved CSV file
    return csv_file_path