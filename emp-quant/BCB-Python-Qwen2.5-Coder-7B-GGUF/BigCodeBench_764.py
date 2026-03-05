
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
        raise TypeError("latin_names must be a list")
    if not isinstance(names, list):
        raise TypeError("names must be a list")
    
    # Set random seed if provided
    if rng_seed is not None:
        random.seed(rng_seed)
    
    # Determine the number of entries
    num_entries = 100
    
    # Create a list to hold the rows
    rows = []
    
    # Add header row
    rows.append(['Name', 'Age'])
    
    # Generate the rows
    for _ in range(num_entries):
        # Randomly choose a name from either list
        if random.choice([True, False]):
            name = random.choice(latin_names)
        else:
            name = random.choice(names)
        
        # Randomly generate an age between 20 and 50
        age = random.randint(20, 50)
        
        # Append the row to the list
        rows.append([name, str(age)])
    
    # Write the rows to the CSV file
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
    
    # Return the CSV file name
    return csv_file