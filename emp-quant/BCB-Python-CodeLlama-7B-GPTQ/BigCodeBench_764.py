import csv
import random
def task_func(csv_file='names.csv', 
          latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
          names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
          encoding='latin-1', rng_seed=None):
    """
    Creates a CSV file with 100 lines. Each line contains a name and an age (randomly generated between 20 and 50). Half of the names are randomly selected from a list of Latin names, the other half from a list of English names. All names are encoded using the specified encoding. If empty name arrays are passed, a csv with headers but no entries is generated.

    Args:
        csv_file (str, optional): Name of the CSV file to be created. Defaults to 'names.csv'.
        latin_names (list, optional): List of Latin names. Defaults to ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'].
        names (list, optional): List of English names. Defaults to ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'].
        encoding (str, optional): The encoding used for writing the names. Defaults to 'latin-1'.
        rng_seed (int, optional): The seed for the rng. Defaults to None.

    Returns:
        str: The CSV file name.

    Raises:
        TypeError: If csv_file is not a string.
        TypeError: If latin_names is not an array.
        TypeError: If names is not an array.
    """
    if not isinstance(csv_file, str):
        raise TypeError('csv_file must be a string')
    if not isinstance(latin_names, list):
        raise TypeError('latin_names must be a list')
    if not isinstance(names, list):
        raise TypeError('names must be a list')

    # Generate random names
    random.seed(rng_seed)
    random_names = random.choices(latin_names + names, k=100)

    # Write to CSV file
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        for name in random_names:
            writer.writerow([name, random.randint(20, 50)])

    return csv_file