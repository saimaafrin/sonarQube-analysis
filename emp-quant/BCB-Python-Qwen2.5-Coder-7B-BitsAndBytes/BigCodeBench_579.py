
import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def normalize_text(text):
    return ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')

def task_func(csv_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            text_data = ' '.join(row[0] for row in reader if row)  # Assuming text is in the first column
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found at the specified path.")
    except IOError:
        raise IOError("Error in reading the file.")

    normalized_text = normalize_text(text_data.lower())
    word_list = normalized_text.split()
    word_count = Counter(word_list)

    most_common_words = word_count.most_common(10)

    fig, ax = plt.subplots()
    ax.bar([word[0] for word in most_common_words], [word[1] for word in most_common_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')

    return (ax, most_common_words)