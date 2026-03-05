
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
    if rng_seed is not None and not isinstance(rng_seed, int):
        raise TypeError("rng_seed must be an integer")

    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])

        for name in latin_names:
            writer.writerow([name, random.randint(20, 50)])

        for name in names:
            writer.writerow([name, random.randint(20, 50)])

    return csv_file