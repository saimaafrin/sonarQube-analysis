
from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os

PUNCTUATION = set(punctuation)

def task_func(text, filename):
    # Tokenize the text using regular expression to capture words
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    tokens = tokenizer.tokenize(text)
    
    # Filter out words that start with '$' and are not solely composed of punctuation
    filtered_words = [word for word in tokens if word.startswith('$') and not all(char in PUNCTUATION for char in word)]
    
    # Create a temporary directory to save the CSV file
    temp_dir = os.path.join(os.getcwd(), 'temp_csv_files')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Define the full path for the CSV file
    csv_file_path = os.path.join(temp_dir, filename)
    
    # Write the filtered words to the CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word'])  # Write the header
        writer.writerows([[word] for word in filtered_words])  # Write the data
    
    return csv_file_path