import csv
import random
def task_func(file_path,
              num_rows,
              gender=['Male', 'Female', 'Non-Binary'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              seed=None):
    if seed is not None:
        random.seed(seed)
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = ['Name', 'Age', 'Gender', 'Country']
        writer.writerow(headers)
        
        if num_rows <= 0:
            return file_path
        
        for _ in range(num_rows):
            name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
            age = random.randint(20, 60)
            gen = random.choice(gender)
            country = random.choice(countries)
            writer.writerow([name, age, gen, country])
    
    return file_path