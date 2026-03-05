from nltk.tokenize import RegexpTokenizer
from string import punctuation
import csv
import os
PUNCTUATION = set(punctuation)
def task_func(text, filename):
    # Tokenize the text to get words
    tokenizer = RegexpTokenizer(r'\b\w+\b')
    words = tokenizer.tokenize(text)
    
    # Filter words that start with '$' and are not solely punctuation
    filtered_words = [word for word in words if word.startswith('$') and not all(char in PUNCTUATION for char in word)]
    
    # Create a temporary directory to save the CSV file
    temp_dir = os.path.join(os.getcwd(), 'temp')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Define the path for the CSV file
    csv_path = os.path.join(temp_dir, filename)
    
    # Write the filtered words to the CSV file
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word'])  # Write the header
        writer.writerows([[word] for word in filtered_words])  # Write the words
    
    # Return the absolute path of the saved CSV file
    return os.path.abspath(csv_path)