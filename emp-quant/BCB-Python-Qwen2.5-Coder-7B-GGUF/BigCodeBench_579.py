
import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def task_func(csv_file):
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            text = ' '.join([row[0] for row in reader])
    except FileNotFoundError:
        raise FileNotFoundError("The CSV file cannot be found at the specified path.")
    except IOError:
        raise IOError("An error occurred while reading the file.")

    normalized_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    word_counts = Counter(normalized_text.split())
    most_common_words = word_counts.most_common(10)

    fig, ax = plt.subplots()
    ax.bar([word[0] for word in most_common_words], [word[1] for word in most_common_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequencies')
    ax.set_title('10 Most Common Words')

    return ax, most_common_words