
import csv
import random

def task_func(csv_file='names.csv', 
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
              encoding='latin-1', rng_seed=None):
    
    # Validate input types
    if not isinstance(csv_file, str):
        raise TypeError("csv_file must be a string")
    if not isinstance(latin_names, list):
        raise TypeError("latin_names must be an array")
    if not isinstance(names, list):
        raise TypeError("names must be an array")
    
    # Set random seed if provided
    if rng_seed is not None:
        random.seed(rng_seed)
    
    # Determine number of entries per name list
    num_entries = 100 // len(latin_names)
    
    # Create data
    data = [['Name', 'Age']]
    for _ in range(num_entries):
        for name_list in [latin_names, names]:
            for _ in range(len(name_list)):
                name = random.choice(name_list)
                age = random.randint(20, 50)
                data.append([name, str(age)])
    
    # Write data to CSV file
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    
    return csv_file