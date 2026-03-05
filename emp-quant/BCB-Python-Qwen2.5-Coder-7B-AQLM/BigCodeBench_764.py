
import csv
import random

def task_func(csv_file='names.csv', 
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
              encoding='latin-1', rng_seed=None):
    if not isinstance(csv_file, str):
        raise TypeError("csv_file must be a string")
    if not isinstance(latin_names, list):
        raise TypeError("latin_names must be an array")
    if not isinstance(names, list):
        raise TypeError("names must be an array")
    
    if rng_seed is not None:
        random.seed(rng_seed)
    
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        for _ in range(50):
            if random.choice([True, False]):
                writer.writerow([random.choice(latin_names), str(random.randint(20, 50))])
            else:
                writer.writerow([random.choice(names), str(random.randint(20, 50))])
    
    return csv_file