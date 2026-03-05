import csv
import random
def task_func(csv_file='names.csv', 
          latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
          names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
          encoding='latin-1', rng_seed=None):
    """
    Create a CSV file with 100 lines. Each line contains a name and an age (randomly generated between 20 and 50). Half of the names are randomly selected from a list of Latin names (default: ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']), the other half from a list of English names (default: ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']). All names are encoded using the specified encoding. If empty name arrays are passed, a csv with headers but no entries is generated.
    Args:
        - csv_file (str, optional): Name of the CSV file to be created. Defaults to 'names.csv'.
        - latin_names (list, optional): List of Latin names. Defaults to ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'].
        - names (list, optional): List of English names. Defaults to ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'].
        - encoding (str, optional): The encoding used for writing the names. Defaults to 'latin-1'
        - rng_seed (int, optional): The seed for the rng. Defaults to None.
    Returns:
        str: The CSV file name.
    Raises:
        TypeError: If csv_file is not a string.
        TypeError: If latin_names is not an array.
        TypeError: If names is not an array.
    """
    # Check if csv_file is a string
    if not isinstance(csv_file, str):
        raise TypeError("csv_file must be a string")

    # Check if latin_names is an array
    if not isinstance(latin_names, list):
        raise TypeError("latin_names must be a list")

    # Check if names is an array
    if not isinstance(names, list):
        raise TypeError("names must be a list")

    # Set the random seed if provided
    if rng_seed is not None:
        random.seed(rng_seed)

    # Create the CSV file
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])

        # Write the Latin names
        for i in range(0, 50, 2):
            writer.writerow([random.choice(latin_names), random.randint(20, 50)])

        # Write the English names
        for i in range(1, 100, 2):
            writer.writerow([random.choice(names), random.randint(20, 50)])

    return csv_file