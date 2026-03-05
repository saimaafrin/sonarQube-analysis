
import csv
import random
from faker import Faker

def task_func(file_path, num_rows, random_seed=None):
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0")
    
    if random_seed is not None:
        random.seed(random_seed)
        Faker.seed(random_seed)
    
    fake = Faker()
    
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        
        for _ in range(num_rows):
            name = fake.name()
            age = random.randint(20, 60)
            address = fake.address().replace('\n', ', ')
            email = fake.email()
            writer.writerow([name, age, address, email])
    
    return file_path