import csv
import random
from faker import Faker
def task_func(file_path, num_rows, random_seed=None):
    # Validate num_rows
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0")
    
    # Initialize Faker with the provided seed if any
    fake = Faker()
    if random_seed is not None:
        fake.seed(random_seed)
    
    # Prepare the data
    data = [['Name', 'Age', 'Address', 'Email']]
    for _ in range(num_rows):
        name = fake.name()
        age = random.randint(20, 60)
        address = fake.address().replace('\n', ', ')
        email = fake.email()
        data.append([name, str(age), address, email])
    
    # Write data to CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    # Return the file path
    return file_path