
import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def task_func(csv_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.extend(row)

        normalized_data = [unicodedata.normalize('NFD', item).encode('ascii', 'ignore').decode('utf-8') for item in data]

        word_counts = Counter(normalized_data)
        most_common_words = word_counts.most_common(10)

        fig, ax = plt.subplots()
        ax.bar([word[0] for word in most_common_words], [word[1] for word in most_common_words])
        ax.set_xlabel('Words')
        ax.set_ylabel('Frequency')
        ax.set_title('10 Most Common Words')

        return ax, most_common_words
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except IOError:
        raise IOError("Error reading the CSV file.")