
import csv
import random

def task_func(csv_file='names.csv', 
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
              encoding='latin-1', rng_seed=None):
    if not isinstance(csv_file, str):
        raise TypeError("csv_file must be a string")
    if not isinstance(latin_names, list):
        raise TypeError("latin_names must be a list")
    if not isinstance(names, list):
        raise TypeError("names must be a list")
    
    if rng_seed is not None:
        random.seed(rng_seed)
    
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        
        for _ in range(100):
            half = 50
            names_list = latin_names + names
            random.shuffle(names_list)
            selected_names = names_list[:half] + names_list[half:]
            selected_names = random.sample(selected_names, 2)
            writer.writerow([selected_names[0], random.randint(20, 50)])
            writer.writerow([selected_names[1], random.randint(20, 50)])
    
    return csv_file