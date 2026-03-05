
import csv
import random
from faker import Faker

def task_func(file_path, num_rows, random_seed=None):
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0")

    faker = Faker()
    names = [faker.name() for _ in range(num_rows)]
    ages = [random.randint(20, 60) for _ in range(num_rows)]
    addresses = [faker.address() for _ in range(num_rows)]
    emails = [faker.email() for _ in range(num_rows)]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        for i in range(num_rows):
            writer.writerow([names[i], ages[i], addresses[i], emails[i]])

    return file_path