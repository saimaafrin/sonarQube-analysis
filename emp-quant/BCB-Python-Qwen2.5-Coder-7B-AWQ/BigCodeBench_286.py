from collections import Counter
import os
import csv
def task_func(output_file, test_directory):
    if not os.path.exists(test_directory):
        return 0

    word_counts = Counter()
    for filename in os.listdir(test_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(test_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                words = file.read().split()
                word_counts.update(words)

    total_words = sum(word_counts.values())
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        for word, count in word_counts.items():
            writer.writerow([word, count])

    return total_words