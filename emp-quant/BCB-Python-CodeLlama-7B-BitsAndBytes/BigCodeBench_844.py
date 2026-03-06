
import csv
import random
from faker import Faker

def task_func(file_path, num_rows, random_seed=None):
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be a positive integer")

    fake = Faker()
    fake.seed(random_seed)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        for _ in range(num_rows):
            name = fake.name()
            age = random.randint(20, 60)
            address = fake.address()
            email = fake.email()
            writer.writerow([name, age, address.replace('\n', ', '), email])

    return file_path