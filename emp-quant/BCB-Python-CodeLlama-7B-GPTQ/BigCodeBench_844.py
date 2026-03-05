import csv
import random
from faker import Faker
def task_func(file_path, num_rows, random_seed=None):
    """
    Generate a CSV file with fake personal data.

    Args:
        file_path (str): The file path of the generated CSV file.
        num_rows (int): The number of rows in the CSV file.
        random_seed (int, optional): The random seed for generating fake data.

    Returns:
        str: The file path of the generated CSV file.

    Raises:
        ValueError: If num_rows is not an integer >= 0.
    """
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0")

    # Generate fake data
    fake = Faker()
    fake.seed_instance(random_seed)
    names = [fake.name() for _ in range(num_rows)]
    ages = [fake.random_int(20, 60) for _ in range(num_rows)]
    addresses = [fake.address() for _ in range(num_rows)]
    emails = [fake.email() for _ in range(num_rows)]

    # Replace newlines in addresses with ','
    for i, address in enumerate(addresses):
        addresses[i] = address.replace("\n", ", ")

    # Write data to CSV file
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Age", "Address", "Email"])
        for name, age, address, email in zip(names, ages, addresses, emails):
            writer.writerow([name, age, address, email])

    return file_path