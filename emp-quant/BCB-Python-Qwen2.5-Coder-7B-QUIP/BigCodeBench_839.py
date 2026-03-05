
import csv
import random

def task_func(file_path,
              num_rows,
              gender=['Male', 'Female', 'Non-Binary'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              seed=None):
    if seed is not None:
        random.seed(seed)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'Gender', 'Country'])

        for _ in range(num_rows):
            name = ''.join(random.choices(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), k=5))
            age = random.randint(20, 60)
            gender_choice = random.choice(gender)
            country_choice = random.choice(countries)
            writer.writerow([name, age, gender_choice, country_choice])

    return file_path