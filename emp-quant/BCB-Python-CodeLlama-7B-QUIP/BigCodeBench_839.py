
import csv
import random

def task_func(file_path,
          num_rows,
          gender=['Male', 'Female', 'Non-Binary'],
          countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
          seed=None):
    if num_rows <= 0:
        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Age', 'Gender', 'Country'])
    else:
        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            for i in range(num_rows):
                name = random.choice(list(string.ascii_uppercase[:5]) + [' '])
                age = random.randint(20, 60)
                gender = random.choice(gender)
                country = random.choice(countries)
                writer.writerow([name, age, gender, country])
    return file_path