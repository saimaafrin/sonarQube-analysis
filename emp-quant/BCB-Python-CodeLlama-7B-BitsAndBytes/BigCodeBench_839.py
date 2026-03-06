
import csv
import random

def task_func(file_path, num_rows, gender=['Male', 'Female', 'Non-Binary'], countries=['USA', 'UK', 'Canada', 'Australia', 'India'], seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Open the CSV file for writing
    with open(file_path, 'w', newline='') as csvfile:
        # Create a CSV writer
        csvwriter = csv.writer(csvfile)

        # Write the headers
        csvwriter.writerow(['Name', 'Age', 'Gender', 'Country'])

        # Generate random data for the rows
        for i in range(num_rows):
            # Generate a random name
            name = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))

            # Generate a random age
            age = random.randint(20, 60)

            # Generate a random gender
            gender = random.choice(gender)

            # Generate a random country
            country = random.choice(countries)

            # Write the row to the CSV file
            csvwriter.writerow([name, age, gender, country])

    # Return the file path of the generated CSV file
    return file_path

# Call the function with the specified parameters
task_func('/test.csv', 100, gender=['test'], countries=['Albania', 'Germany', 'Austria'], seed=12)