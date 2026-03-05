import csv
import random
from faker import Faker
def task_func(file_path, num_rows, random_seed=None):
    """
    Generate a CSV file with fake personal data.

    Args:
        file_path (str): The file path of the generated CSV file.
        num_rows (int): The number of rows in the CSV file.
        random_seed (int, optional): The random seed to use. Defaults to None.

    Returns:
        str: The file path of the generated CSV file.

    Raises:
        ValueError: If num_rows is not an integer >= 0.
    """
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0")

    # Set the random seed if provided
    if random_seed is not None:
        random.seed(random_seed)

    # Create a Faker object
    fake = Faker()

    # Create a CSV writer
    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(["Name", "Age", "Address", "Email"])

        # Write the data rows
        for _ in range(num_rows):
            name = fake.name()
            age = random.randint(20, 60)
            address = fake.address()
            email = fake.email()
            writer.writerow([name, age, address, email])

    return file_path