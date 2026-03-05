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

    # Open the CSV file for writing
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(['Name', 'Age'])
        # Generate and write the rows
        for _ in range(50):  # Half of the lines
            name = random.choice(latin_names)
            age = random.randint(20, 50)
            writer.writerow([name, age])
        for _ in range(50):  # The other half of the lines
            name = random.choice(names)
            age = random.randint(20, 50)
            writer.writerow([name, age])

    return csv_file