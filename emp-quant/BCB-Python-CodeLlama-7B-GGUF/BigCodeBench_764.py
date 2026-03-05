
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

    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])

        rng = random.Random()
        if rng_seed is not None:
            rng.seed(rng_seed)

        for i in range(100):
            name = rng.choice(latin_names) if rng.randint(0, 1) else rng.choice(names)
            age = rng.randint(20, 50)
            writer.writerow([name, age])

    return csv_file